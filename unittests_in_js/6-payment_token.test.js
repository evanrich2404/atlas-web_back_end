const { expect } = require('chai');
const { getPaymentTokenFromAPI } = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('resolves with the correct object when success is true', function(done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => done(error));
  });

  it('returns a promise that resolves with the correct object when success is true', function() {
    return getPaymentTokenFromAPI(true).then((response) => {
      expect(response).to.deep.equal({ data: 'Successful response from the API' });
    });
  });
});
