#!/usr/bin/python

from park.api.api import API

class Delegate(API):
    def count(self):
        return self.get('api/delegates/count')

    def search(self, q, parameters={}):
        return self.get('api/delegates/search', compact('q') + parameters)

    def voters(self, publicKey, parameters={}):
        return self.get('api/delegates/voters', compact('publicKey') + parameters)

    def delegate(self, parameters={}):
        return self.get('api/delegates/get', parameters)

    def delegates(self, parameters={}):
        return self.get('api/delegates', parameters)

    def fee(self):
        return self.get('api/delegates/fee')

    def forgedByAccount(self, generatorPublicKey):
        return self.get('api/delegates/forging/getForgedByAccount', {
            "generatorPublicKey" : generatorPublicKey
        })

    def create(self, secret, username, secondSecret=None):
        transaction = self.client.delegateBuilder().create(
            secret, username, secondSecret
        )

        return self.post('peer/transactions', { "transactions": [transaction] })

    def nextForgers(self):
        return self.get('api/delegates/getNextForgers')

    def enableForging(self, secret, parameters={}):
        return self.post('api/delegates/forging/enable', {
            **{ "secret" : secret }, **parameters
        })

    def disableForging(self, secret, parameters={}):
        return self.post('api/delegates/forging/disable', {
            **{ "secret" : secret }, **parameters
        })

    def forgingStatus(self, publicKey, parameters={}):
        return self.get('api/delegates/forging/status', {
            **{ "publicKey" : publicKey }, **parameters
        })
