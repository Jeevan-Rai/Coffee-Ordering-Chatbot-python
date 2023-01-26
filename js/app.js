// Handle user input and send to Python for processing
document.querySelector("#chatbot-form").addEventListener("submit", function (event) {
    event.preventDefault();
    let userInput = document.querySelector("#chatbot-input").value;
    // Send user input to Python via a fetch or XHR request
    fetch("/process-input", {
        method: "POST",
        body: JSON.stringify({ input: userInput }),
        headers: { "Content-Type": "application/json" }
    })
        .then(response => response.json())
        .then(data => {
            // Display response from Python in the chatbot messages container
            let messagesContainer = document.querySelector("#chatbot-messages");
            messagesContainer.innerHTML += `<div>${data.response}</div>`;
        });
});
