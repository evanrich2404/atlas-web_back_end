const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('correctly rounds a and b and sums them (1.2, 3.4)', function() {
    assert.strictEqual(calculateNumber(1.2, 3.4), 4);
  });

  it('correctly rounds a and b and sums them (1.8, 3.0)', function() {
    assert.strictEqual(calculateNumber(1.8, 3.0), 5);
  });

  it('correctly rounds a and b and sums them (1.0, 3.5)', function() {
    assert.strictEqual(calculateNumber(1.0, 3.5), 5);
  });

  it('correctly rounds a and b and sums them (1.6, 3.9)', function() {
    assert.strictEqual(calculateNumber(1.6, 3.9), 6);
  });

  // Add more test cases as needed
});
