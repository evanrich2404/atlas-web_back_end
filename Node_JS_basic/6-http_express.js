const express = require('express');

// Create an Express application
const app = express();

// Define a route for the root URL '/'
app.get('/', (req, res) => {
  // Send "Hello Holberton School!" to the client
  res.send('Hello Holberton School!');
});

// Make the application listen on port 1245
app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

// Export ze app
module.exports = app;
