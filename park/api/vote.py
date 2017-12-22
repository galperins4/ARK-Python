#!/usr/bin/python

from park.api.api import API

class Vote(API):
    def vote(secret, delegate, secondSecret=None):
        transaction = self.client.voteBuilder().create(secret, delegate, secondSecret)

        return self.post('peer/transactions', { "transactions": [transaction] })

    def unvote(secret, delegate, secondSecret=None):
        transaction = self.client.voteBuilder().delete(secret, delegate, secondSecret)

        return self.post('peer/transactions', { "transactions": [transaction] })
