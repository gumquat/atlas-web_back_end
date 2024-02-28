// testing cases for 'Spies'

const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it ('should return 200 if the payment is successful', () => {
      const spy = sinon.spy(Utils, 'calculateNumber');

      sendPaymentRequestToApi(100, 20);

      expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
      spy.restore();
  });
});
