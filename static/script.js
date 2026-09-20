const input = document.getElementById("messageInput");
const chatBox = document.getElementById("chatBox");

input.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

async function sendMessage() {

    const message = input.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user");

    input.value = "";

    const loading = addMessage("Thinking...", "ai");

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        loading.remove();

        if (data.error) {
            addMessage("Error: " + data.error, "ai");
            return;
        }

        addMessage(data.reply, "ai");

    } catch (error) {

        loading.remove();

        addMessage(
            "Something went wrong. Please check the server.",
            "ai"
        );

        console.error(error);
    }
}

function addMessage(text, type) {

    const message = document.createElement("div");

    message.className = `message ${type}`;

    message.innerHTML = `
        <div class="bubble"></div>
    `;

    message.querySelector(".bubble").textContent = text;

    chatBox.appendChild(message);

    chatBox.scrollTop = chatBox.scrollHeight;

    return message;
}