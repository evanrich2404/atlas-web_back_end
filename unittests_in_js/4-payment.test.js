const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi with Stub', function () {
  let consoleSpy, calculateNumberStub;

  beforeEach(() => {
    // Stub the Utils.calculateNumber function to always return 10
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    // Spy on console.log to verify output
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the original functionality after each test
    calculateNumberStub.restore();
    consoleSpy.restore();
  });

  it('should log the correct message with a stubbed return value of 10', function () {
    sendPaymentRequestToApi(100, 20);

    // Check if the stub was called with the expected arguments
    expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;
    // verify that console.log was called with the expected message
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
  });
});
