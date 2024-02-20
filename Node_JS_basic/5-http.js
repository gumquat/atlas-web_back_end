const http = require('http');
const url = require('url');
const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const rows = data.split('\n').filter(Boolean);
    const headers = rows.shift().split(',');
    const fieldIndex = headers.indexOf('field');
    const firstNameIndex = headers.indexOf('firstname');
    const fields = [...new Set(rows.map((row) => row.split(',')[fieldIndex]))];

    let result = `Number of students: ${rows.length}\n`;

    fields.forEach((field) => {
      const students = rows.filter((row) => row.split(',')[fieldIndex] === field);
      result += `Number of students in ${field}: ${students.length}. List: ${students.map((student) => student.split(',')[firstNameIndex]).join(', ')}\n`;
    });

    return result;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  const q = url.parse(req.url, true).path;
  if (q === '/') {
    res.write('Hello Holberton School!');
    res.end();
  }
  if (q === '/students') {
    res.write('This is the list of our students\n');
    try {
      const data = await countStudents(process.argv[2]);
      res.write(data);
    } catch (error) {
      res.write(error.message);
    } finally {
      res.end();
    }
  }
});

app.listen(1245);
module.exports = app;
