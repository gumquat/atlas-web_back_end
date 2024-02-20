const { readDatabase } = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const data = await readDatabase();
      const studentsByField = {};
      
      data.forEach(student => {
        const field = student.field.toLowerCase();
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(student.firstname);
      });

      const sortedFields = Object.keys(studentsByField).sort();
      let responseText = 'This is the list of our students\n';

      sortedFields.forEach(field => {
        const studentsCount = studentsByField[field].length;
        const firstNamesList = studentsByField[field].join(', ');
        responseText += `Number of students in ${field}: ${studentsCount}. List: ${firstNamesList}\n`;
      });

      res.status(200).send(responseText);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.query;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const data = await readDatabase();
      const studentsInMajor = data
        .filter(student => student.field.toLowerCase() === major.toLowerCase())
        .map(student => student.firstname)
        .join(', ');

      res.status(200).send(`List: ${studentsInMajor}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
