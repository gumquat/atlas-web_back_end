// 1-stdin.js
// program that will be executed through command line, displaying messages
// and displays user input

// Program that displays a string, takes inputs, and responds

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('readable', () => {
  const name = process.stdin.read();
  if (name) {
    process.stdout.write(`Your name is: ${name}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});

/**
the code below fails ONE check but OTHERWISE WORKS FINE
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
*/
