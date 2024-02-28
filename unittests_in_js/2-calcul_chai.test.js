// test using 'Chai' (an assertion library)

const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return the sum of two rounded numbers', function() {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  });

  describe('SUBTRACT', function() {
    it('should return the result of subtracting the second rounded number from the first', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
  });

  describe('DIVIDE', function() {
    it('should return the result of dividing the first rounded number by the second', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when attempting to divide by 0', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
  });

  // more error handling
  describe('Edge Cases and Error Handling', function() {

    it('should round half towards positive infinity', function() {
      expect(calculateNumber('SUM', 1.5, 2.5)).to.equal(5);
      expect(calculateNumber('SUBTRACT', 2.5, 1.5)).to.equal(1);
    });
  });
});
