const http = require('http');
const fs = require('fs').promises;

// Function to read and process the database file asynchronously
function countStudents(path) {
  return fs.readFile(path, { encoding: 'utf8' })
    .then((data) => {
      let message = 'This is the list of our students\n';
      const lines = data.split('\n').filter((line) => line);
      lines.shift(); // remove header

      const students = lines.map((line) => {
        const [firstName, , , field] = line.split(',');
        return { firstName, field };
      });

      const fields = {};
      students.forEach((student) => {
        if (!fields[student.field]) {
          fields[student.field] = [];
        }
        fields[student.field].push(student.firstName);
      });

      message += `Number of students: ${students.length}\n`;
      // eslint-disable-next-line guard-for-in
      for (const field in fields) {
        message += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      }

      return message.trim();
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

// Create an HTTP server
const app = http.createServer((req, res) => {
  // Request '/' for Holberton Salutations
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
    // Request '/students' for list of students
  } else if (req.url === '/students') {
    countStudents('database.csv')
      .then((message) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(message);
      })
      // Error message if not working
      .catch((error) => {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(error.message);
      });
    // error message if not found
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Page not found');
  }
});
// Listening on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the server
module.exports = app;
