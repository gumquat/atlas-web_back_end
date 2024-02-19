// 0-console.js
// function named displayMessage that prints in STDOUT the string argument

function displayMessage(message) {
  // output the given data as a message to the console
  console.log(message);
}

//allows other files to use the function 'displayMessage'
module.exports = displayMessage;
