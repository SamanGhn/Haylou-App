# استفاده از ایمیج پایه پایتون
FROM python:3.11-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های مورد نیاز
COPY requirements.txt .

# نصب پکیج‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی بقیه فایل‌ها
COPY . .

# اجرا با eventlet
CMD ["python", "app.py"]

