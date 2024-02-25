// Test cases of 'calculateNumber'
// assuming a and b are numbers

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should return the sum of rounded a and b', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return the sum when one is rounded up and the other is rounded down', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return the sum when both are rounded up', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should handle rounding up to the next integer correctly', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  
  it('should handle negative numbers correctly', function() {
    assert.strictEqual(calculateNumber(-1, -2), -3);
    assert.strictEqual(calculateNumber(-1.4, 2.6), 2);
  });

  it('should return the sum when both numbers are decimals', function() {
    assert.strictEqual(calculateNumber(0.1, 0.2), 0);
    assert.strictEqual(calculateNumber(0.9, 1.1), 2);
  });

  it('should return the first number when the second one is 0 after rounding', function() {
    assert.strictEqual(calculateNumber(1.2, 0.49), 1);
  });

  it('should return the second number when the first one is 0 after rounding', function() {
    assert.strictEqual(calculateNumber(0.49, 2.5), 3);
  });

  it('should handle zero correctly', function() {
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(0, 2.9), 3);
  });
});