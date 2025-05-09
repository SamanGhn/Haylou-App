from flask import Flask, request
from flask_socketio import SocketIO, emit
import psycopg2
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

# اتصال به دیتابیس
conn = psycopg2.connect(
    dbname=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host='db',  # اسم سرویس در docker-compose
    port='5432'
)
cursor = conn.cursor()

# ایجاد جدول اگر وجود نداشت
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    username TEXT,
    message TEXT,
    timestamp TIMESTAMP DEFAULT NOW()
)
""")
conn.commit()

# هندل اتصال کلاینت
@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit("message", {"user": "server", "text": "Welcome to Haylou Chat!"})

# هندل پیام‌ها
@socketio.on('message')
def handle_message(data):
    username = data.get('user', 'Anonymous')
    msg = data['text']
    cursor.execute("INSERT INTO messages (username, message) VALUES (%s, %s)", (username, msg))
    conn.commit()
    emit('message', {"user": username, "text": msg}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
