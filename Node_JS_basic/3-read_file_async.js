const fs = require('fs').promises; // Note the use of .promises

function countStudents(path) {
  return fs.readFile(path, { encoding: 'utf8' })
    .then((data) => {
      // Process the file content
      const lines = data.split('\n').filter(line => line !== '');
      lines.shift(); // Remove the header row

      const students = lines.map(line => {
        const [firstName, , , field] = line.split(',');
        return { firstName, field };
      });

      // Count the total number of students
      console.log(`Number of students: ${students.length}`);

      // Process each field
      const fields = {};
      students.forEach(student => {
        if (!fields[student.field]) {
          fields[student.field] = [];
        }
        fields[student.field].push(student.firstName);
      });

      Object.keys(fields).forEach(field => {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      });

      // Return a meaningful result, if needed
      return `Processed ${students.length} students`;
  })
  .catch((error) => {
      // If the file does not exist or cannot be read, throw an error
      throw new Error('Cannot load the database');
  });
}

module.exports = countStudents
