const express = require('express');
const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const rows = data.split('\n').filter(Boolean);
    const headers = rows.shift().split(',');
    const fieldIndex = headers.indexOf('field');
    const firstNameIndex = headers.indexOf('firstname');
    const fields = [...new Set(rows.map(row => row.split(',')[fieldIndex]))];

    let result = `Number of students: ${rows.length}\n`;

    fields.forEach(field => {
      const students = rows.filter(row => row.split(',')[fieldIndex] === field);
      result += `Number of students in ${field}: ${students.length}. List: ${students.map(student => student.split(',')[firstNameIndex]).join(', ')}\n`;
    });

    return result;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const data = await countStudents(process.argv[2]);
    res.send(`This is the list of our students\n${data}`);
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(port, () => {
  console.log(`Listening on port ${port}.`);
});

module.exports = app;
