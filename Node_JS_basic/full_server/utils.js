const fs = require('fs').promises;

async function readDatabase(path) {
  try {
    // Attempt to read the file at the given path asynchronously.
    const data = await fs.readFile(path, { encoding: 'utf8' });
    // Split the file content into lines.
    const lines = data.split('\n').filter((line) => line.trim());

    // Remove the first line (header) from the lines array.
    lines.shift();

    // Process each line to organize students by field.
    const fields = lines.reduce((acc, line) => {
      // Extract the student's first name and field of study from the line.
      const [firstName, , , field] = line.split(',');
      // Initialize the array for this field if it does not exist.
      if (!acc[field]) {
        acc[field] = [];
      }
      // Add the student's first name to the field's array.
      acc[field].push(firstName);
      return acc;
    }, {});

    // Return the organized data as an object of arrays.
    return fields;
  } catch (Error) {
    // If an error occurs (e.g., file not found),
    // throw a new error indicating the database could not be loaded.
    throw new Error('Cannot load the database');
  }
}

module.exports = { readDatabase };
