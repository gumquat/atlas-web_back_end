const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return the sum of two rounded numbers', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });

  describe('SUBTRACT', function() {
    it('should return the result of subtracting the second rounded number from the first', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
  });

  describe('DIVIDE', function() {
    it('should return the result of dividing the first rounded number by the second', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when attempting to divide by 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });

  // more error handling
  describe('Edge Cases and Error Handling', function() {

    it('should round half towards positive infinity', function() {
      assert.strictEqual(calculateNumber('SUM', 1.5, 2.5), 5);
      assert.strictEqual(calculateNumber('SUBTRACT', 2.5, 1.5), 1);
    });
  });
});
