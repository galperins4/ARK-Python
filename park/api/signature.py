#!/usr/bin/python

from park.api.api import API

class Signature(API):
    def fee(self):
        return self.get('api/signatures/fee')

    def create(self, secret, secondSecret):
        transaction = self.client.signatureBuilder().create(secret, secondSecret)

        return self.post('peer/transactions', { "transactions": [transaction] })
