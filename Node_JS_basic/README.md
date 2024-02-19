# NodeJS Basics Project Repository

## Pre-Work Information

### Running JavaScript using Node.js

To execute JavaScript code using Node.js, follow these steps:

1. Install Node.js from [Node.js official website](https://nodejs.org/).
2. Write your JavaScript code in a `.js` file.
3. Open a terminal or command prompt.
4. Navigate to the directory containing your JavaScript file.
5. Run the command: `node filename.js`

### Using Node.js Modules

Node.js uses a module system to organize code. You can import modules using the `require` keyword. Example:

```
javascript
const fs = require('fs');
```

### Using a Specific Node.js Module to Read Files

To read files in Node.js, you can use the built-in fs module. Here's an example:
```
const fs = require('fs');

fs.readFile('filename.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
```

### Using Process to Access Command Line Arguments and Environment Variables

Node.js provides the process global object to access command line arguments and environment variables. Example:
```
// Accessing command line arguments
console.log(process.argv);

// Accessing environment variables
console.log(process.env.SOME_VARIABLE);

```

### Creating a Small HTTP Server using Node.js

You can create a basic HTTP server using the built-in http module. Example:

```
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World!');
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

### Creating a Small HTTP Server using Express.js

Express.js is a popular web application framework for Node.js. <br>
To create an HTTP server using Express.js, first, install Express.js:
```
npm install express
```
Then, create a server with Express.js:
```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

### Creating Advanced Routes with Express.js

Express.js allows you to create advanced routes using various HTTP methods and route parameters. Example:
```
app.get('/users/:userId', (req, res) => {
  const userId = req.params.userId;
  // Logic to fetch user data
  res.send(`User ID: ${userId}`);
});
```

### Using ES6 with Node.js with Babel-node

To use ES6 features in Node.js, you can use Babel to transpile your code. First, install Babel:
```
npm install @babel/core @babel/node @babel/preset-env --save-dev
```
Then, create a .babelrc file in your project root:
```
{
  "presets": ["@babel/preset-env"]
}
```
Now, you can run your Node.js code using Babel:
```
npx babel-node yourfile.js
```