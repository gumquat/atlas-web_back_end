const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    // split the data into rows
    // remove empty lines
    const rows = data.split('\n').filter(row => row.trim());

    // extract headers from the header row
    const [headerRow, ...studentRows] = rows;
    const headers = headerRow.split(',');

    // find index of 'field' and 'firstname' in the header
    const fieldIndex = headers.indexOf('field');
    const firstNameIndex = headers.indexOf('firstname');

    // get count of total number of students
    console.log(`Number of students: ${studentRows.length}`);

    // group students by field
    // count them
    const studentsByField = studentRows.reduce((acc, row) => {
      const fields = row.split(',');
      const field = fields[fieldIndex];
      if (!acc[field]) {
        acc[field] = [];
      }
      acc[field].push(fields[firstNameIndex]);
      return acc;
    }, {});

    // print number of students in each field, include their names
    for (const field in studentsByField) {
      const students = studentsByField[field];
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
