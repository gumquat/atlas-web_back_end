const express = require('express');
const app = express();
const routes = require('./routes');

const PORT = 1245;

app.use('/', routes);

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});
