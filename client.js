// // Client-Side JavaScript
// const socket = io('http://localhost:5000');

// socket.on('connect', () => {
//     console.log('Connected to server');
// });

// function sendUserInput(input) {
//     socket.emit('user_input', { input: input });
// }

// socket.on('response', (data) => {
//     console.log('Response from server:', data.response);
//     // Display the response in the HTML
//     document.getElementById('response').innerText = data.response;
// });

// Client-Side JavaScript
const socket = io('http://localhost:5000');

socket.on('connect', () => {
    console.log('Connected to server');
});

function sendMessage() {
    const inputElement = document.getElementById('userInput');
    const userInput = inputElement.value;
    socket.emit('user_input', { input: userInput });
}

socket.on('response', (data) => {
    document.getElementById('responseOutput').innerText = `Response: ${data.response}`;
    console.log('Response from server:', data.response);
});
