const fs = require('fs');

function countStudents(path) {
  try {
    // Attempt to read the file synchronously
    const data = fs.readFileSync(path, { encoding: 'utf8' });

    // Split the data into lines
    const lines = data.split('\n').filter((line) => line !== '');

    // Remove the header row
    lines.shift();

    const students = lines.map((line) => {
      const [firstName, , , field] = line.split(',');
      return { firstName, field };
    });

    // Count the total number of students
    console.log(`Number of students: ${students.length}`);

    // Process each field
    const fields = {};
    students.forEach((student) => {
      if (!fields[student.field]) {
        fields[student.field] = [];
      }
      fields[student.field].push(student.firstName);
    });

    Object.keys(fields).forEach((field) => {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    });
  } catch (error) {
    throw new Error('Cannot load  the database');
  }
}

module.exports = countStudents;
