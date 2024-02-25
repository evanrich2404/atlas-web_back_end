// simple program to ask for someone's name

// Import from readline module
const readline = require('readline');

// reusing displayMessage from task 0
const displayMessage = require('./0-console');

// Create an interface for input and output
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Ask the user for their name
displayMessage("Welcome to Holberton School, what is your name?");

// Section to input their name
rl.question('', (name) => {
  // Display the name using displayMessage
  displayMessage(`Your name is: ${name}`);

  //Close the readline interface
  rl.close();
});

// Listen for the 'close' event
rl.on('close', () => {
  // Use displayMessage for the closing message
  displayMessage("This important software is now closing");
});


