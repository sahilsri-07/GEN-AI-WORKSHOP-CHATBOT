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

function askBot() {
    const city = document.getElementById("city").value;
    if (!city) return;

    document.getElementById("msg").value = "hotel in " + city;
    sendMsg();
}