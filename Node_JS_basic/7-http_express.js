const express = require('express');
const fs = require('fs').promises;

// Function to asynchronously read from the database and format the response
async function countStudents(path) {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });
    let message = 'This is the list of our students\n';
    const lines = data.split('\n').filter((line) => line);

    // Ignore the header and empty lines
    lines.shift();

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
    Object.entries(fields).forEach(([field, names]) => {
      message += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    });

    return message.trim();
  } catch (Error) {
    throw new Error('Cannot load the database');
  }
}

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const message = await countStudents('database.csv');
    res.send(message);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

module.exports = app;
