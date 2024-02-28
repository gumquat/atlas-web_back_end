// more Hook stuff

const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
    let spyConsole;

    beforeEach(() => {
        spyConsole = sinon.spy(console, 'log');
    });

    afterEach(() => {
        spyConsole.restore();
    });

    it ('should log "The total is: 120" for inputs 100 and 20', () => {
        sendPaymentRequestToApi(100, 20);
        sinon.assert.calledWithExactly(spyConsole, 'The total is: 120');
    });

    it ('should log "The total is: 20" for inputs 10 and 10', () => {
        sendPaymentRequestToApi(10, 10);
        sinon.assert.calledWithExactly(spyConsole, 'The total is: 20');
    });
});
