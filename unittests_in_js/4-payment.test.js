// testing with 'Stubs'

const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('should return 200 if the payment is successful', () => {
    // Stub the calculateNumber function to always return 10
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Spy on console.log to verify it logs the correct message
    const logSpy = sinon.spy(console, 'log');

    // Execute the function under test
    sendPaymentRequestToApi(100, 20);

    // Verify the stub was called with the expected arguments
    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    // Verify that console.log was called with the expected message
    expect(logSpy.calledWith('The total is: 10')).to.be.true;

    // Restore the original functions to prevent side effects
    stub.restore();
    logSpy.restore();
  });
});
