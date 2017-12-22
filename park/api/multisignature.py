#!/usr/bin/python

from park.api.api import API

class MultiSignature(API):
    def pending(self, publicKey):
        return self.get('api/multisignatures/pending', { "publicKey" : publicKey })

    def sign(self, transactionId, secret, additional={}):
        return self.post('api/multisignatures/sign', {
            **{ "transactionId" : transactionId, "secret" : secret },
            **additional
        })

    def create(self, secret, secondSecret, keysgroup, lifetime, min):
        transaction = self.client.multiSignatureBuilder().create(
            secret, secondSecret, keysgroup, lifetime, min
        )

        return self.post('peer/transactions', { "transactions": [transaction] })

    def accounts(self, publicKey):
        return self.get('api/multisignatures/accounts', { "publicKey" : publicKey })
