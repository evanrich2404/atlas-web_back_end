const { readDatabase } = require('../utils');

class StudentController {
  static async getAllStudents(req, res) {
    try {
      const filePath = '../../database.csv';
      const data = await readDatabase(filePath);

      let responseMessage = 'This is the list of our students\n';
      // Sort fields alphabetically
      const fields = Object.keys(data).sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base' }));

      fields.forEach((field) => {
        const students = data[field];
        responseMessage += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      });

      return res.status(200).send(responseMessage);
    } catch (error) {
      console.error(error);
      return res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }
    try {
      const fields = await readDatabase('../../database.csv');
      if (fields[major]) {
        const response = `List: ${fields[major].join(', ')}`;
        return res.status(200).send(response);
      }
      return res.status(500).send(`Cannot find students in ${major}`);
    } catch (error) {
      return res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentController;
