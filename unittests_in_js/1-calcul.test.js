const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('sums two rounded numbers', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });

  describe('SUBTRACT', function() {
    it('subtracts two rounded numbers', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
  });

  describe('DIVIDE', function() {
    it('divides two rounded numbers', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('returns "Error" when attempting to divide by rounded 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });
});
