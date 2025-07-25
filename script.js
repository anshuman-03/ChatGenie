document.getElementById('chat-form').onsubmit = async function(e) {
    e.preventDefault();
    const msgBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    let userMsg = userInput.value.trim();
    if (!userMsg) return;

    // Display user message
    msgBox.innerHTML += `<div class="msg user">${userMsg}</div>`;
    msgBox.scrollTop = msgBox.scrollHeight;

    userInput.value = '';
    userInput.disabled = true;

    const response = await fetch('/ask', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: userMsg})
    });
    const data = await response.json();

    // Display bot reply
    msgBox.innerHTML += `<div class="msg bot">${data.reply}</div>`;
    msgBox.scrollTop = msgBox.scrollHeight;
    userInput.disabled = false;
    userInput.focus();
};
