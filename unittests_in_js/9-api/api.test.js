// integration test

const expect = require('chai').expect;
const request = require('request');

describe('Index page', function() {
  // Existing tests for the index page
});

// New test suite for the cart page
// Not sure if my error is here or not....
describe('Cart page', function() {
  it('returns status code 200 when :id is a number', function(done) {
    request('http://localhost:7865/cart/12', function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('returns status code 404 when :id is NOT a number', function(done) {
    request('http://localhost:7865/cart/hello', function(error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
