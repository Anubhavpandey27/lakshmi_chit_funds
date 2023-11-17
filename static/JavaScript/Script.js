function toggleChat() {
    const chatbotWindow = document.getElementById('chatbotWindow');
    chatbotWindow.classList.toggle('show');
}

function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    // Implement logic to handle user messages and display responses
    displayUserMessage(userInput);
    // Call a function to process the user's input (e.g., API calls, stock data retrieval)
    processUserInput(userInput);
}

function displayUserMessage(message) {
    const chatMessages = document.getElementById('chatMessages');
    const userDiv = document.createElement('div');
    userDiv.className = 'message user-message';
    userDiv.innerHTML = `<p>${message}</p>`;
    chatMessages.appendChild(userDiv);
}

// Function to display bot's response (can be dynamically generated based on input)
function displayBotResponse(response) {
    const chatMessages = document.getElementById('chatMessages');
    const botDiv = document.createElement('div');
    botDiv.className = 'message bot-message';
    botDiv.innerHTML = `<p>${response}</p>`;
    chatMessages.appendChild(botDiv);
}

function processUserInput(input) {
    // Implement logic to handle user input and generate bot responses (e.g., stock queries)
    // You might use APIs, algorithms, or databases to generate responses
    // Example:
    const botResponse = generateBotResponse(input);
    displayBotResponse(botResponse);
}

function generateBotResponse(input) {
    // Logic to generate bot response based on user input
    // Example response:
    return "This is an example bot response.";
}
