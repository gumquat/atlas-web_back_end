// 1-stdin.js
// program that will be executed through command line, displaying messages
// and includes user input
// used as child process

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', data => {
    console.log(`Your name is: ${data.toString()}`);
    console.log('This important software is now closing')
    process.exit();
    });