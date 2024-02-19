// 1-stdin.js
// program that will be executed through command line, displaying messages
// and displays user input

// display welcome message
console.log('Welcome to Holberton School, what is your name?');

// read user input from standard input 'stdin'
process.stdin.on('data', (data) => {
  // remove trailing newline character from input
  const name = data.toString().trim();

  // display the user's input
  console.log(`Your name is: ${name}`);
});

// display closing message when user chooses to 'end' it
process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
