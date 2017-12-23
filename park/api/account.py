#!/usr/bin/env python

from park.api.api import API

class Account(API):
    def balance(self, address):
        return self.get('api/accounts/getBalance', { "address": address })

    def publickey(self, address):
        return self.get('api/accounts/getPublickey', { "address": address })

    def delegates(self, address):
        return self.get('api/accounts/delegates', { "address": address })

    def delegatesFee(self, address):
        return self.get('api/accounts/delegates/fee', { "address": address })

    def vote(self, secret, publicKey, secondSecret):
        return self.put('api/accounts/delegates', {
            "secret": secret,
            "publicKey": publicKey,
            "secondSecret": secondSecret
        })

    def account(self, address):
        return self.get('api/accounts', { "address": address })

    def accounts(self):
        return self.get('api/accounts/getAllAccounts')

    def top(self):
        return self.get('api/accounts/top')

    def count(self):
        return self.get('api/accounts/count')
