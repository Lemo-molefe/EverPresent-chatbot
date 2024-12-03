async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const response = await fetch(`/chat/?message=${userInput}`);
    const data = await response.json();

    const chatLog = document.getElementById("chat-log");
    chatLog.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    chatLog.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
    document.getElementById("user-input").value = "";
}
 
    
