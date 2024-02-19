// define function 'countStudents'
const fs = require('fs');

function countStudents(path) {
  try {
    // read the database file synchronously
    const data = fs.readFileSync(path, 'utf8');
    
    // split the data into lines and filter out empty lines
    const lines = data.split('\n').filter(line => line.trim() !== '');
    
    // count the total number of students
    const totalStudents = lines.length - 1; // exclude header line
    
    console.log(`Number of students: ${totalStudents}`);
    
    // extract field names from the header line
    const fields = lines[0].split(',');
    
    // count the number of students in each field
    for (let i = 1; i < fields.length; i++) {
      const fieldName = fields[i];
      const studentsInField = lines.slice(1).reduce((count, line) => {
        const values = line.split(',');
        return values[i].trim() !== '' ? count + 1 : count;
      }, 0);
      const studentsList = lines.slice(1)
                                .map(line => line.split(',')[i].trim())
                                .filter(name => name !== '')
                                .join(', ');

      console.log(`Number of students in ${fieldName}: ${studentsInField}. List: ${studentsList}`);
    }
  } catch (error) {
    // throw error if database is not available
    throw new Error('Cannot load the database');
  }
}
