const socket = io("http://localhost:5000"); // در داکر آدرس فرق خواهد کرد

socket.on("message", data => {
  const chat = document.getElementById("chat");
  const message = `<p><strong>${data.user}:</strong> ${data.text}</p>`;
  chat.innerHTML += message;
  chat.scrollTop = chat.scrollHeight;
});

function sendMessage() {
  const user = document.getElementById("username").value || "Anonymous";
  const text = document.getElementById("message").value;
  socket.emit("message", { user, text });
  document.getElementById("message").value = "";
}
