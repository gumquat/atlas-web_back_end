// even mooore integration testing

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

app.get('/available_payments', function (req, res) {
  res.json({
      payment_methods: {
          credit_cards: true,
          paypal: false
      }
  });
});

app.post('/login', function (req, res) {
  const userName = req.body.userName;
  res.send(`Welcome ${userName}`);
});

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
