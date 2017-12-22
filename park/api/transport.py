#!/usr/bin/python

from park.api.api import API

class Transport(API):
    def list(self):
        return self.get('peer/list')

    def blocksCommon(self, ids):
        return self.get('peer/blocks/common', { "ids" : ','.join(ids) })

    def block(self, id):
        return self.get('peer/block', { "id" : id })

    def blocks(self):
        return self.get('peer/blocks')

    def createBlock(self, block):
        return self.post('peer/blocks', { "block" : block })

    def transactions(self):
        return self.get('peer/transactions')

    def transactionsFromIds(self, ids):
        return self.get('peer/transactionsFromIds', { "ids" : ','.join(ids) })

    def createTransactions(self, transactions):
        return self.post('peer/transactions', { "transactions": [transaction] })

    def height(self):
        return self.get('peer/height')

    def status(self):
        return self.get('peer/status')
