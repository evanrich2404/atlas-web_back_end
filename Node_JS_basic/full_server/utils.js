const fs = require('fs').promises;

async function readDatabase(path) {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });
    // Process the data
    return {}; // return an object of arrays
  } catch (Error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = { readDatabase };
