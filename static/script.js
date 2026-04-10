function toggleChat() {
    const box = document.getElementById("chatbox");
    box.style.display = box.style.display === "flex" ? "none" : "flex";
}

function sendMsg() {
    const input = document.getElementById("msg");
    const chat = document.getElementById("chatBody");

    const text = input.value.trim();
    if (!text) return;

    chat.innerHTML += `<div class="user">${text}</div>`;
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: text})
    })
    .then(res => res.json())
    .then(data => {
        chat.innerHTML += `<div class="bot">${data.response}</div>`;
        chat.scrollTop = chat.scrollHeight;
    });
}