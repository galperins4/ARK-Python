#!/usr/bin/python

from park.api.account import Account
from park.api.block import Block
from park.api.delegate import Delegate
from park.api.loader import Loader
from park.api.multisignature import MultiSignature
from park.api.peer import Peer
from park.api.signature import Signature
from park.api.transaction import Transaction
from park.api.transport import Transport
from park.api.vote import Vote

from park.builder.delegate import DelegateBuilder
from park.builder.multisignature import MultiSignatureBuilder
from park.builder.signature import SignatureBuilder
from park.builder.transaction import TransactionBuilder
from park.builder.vote import VoteBuilder

class Park:
    def __init__(self, ip, port, nethash, version):
        self.ip = ip
        self.port = port
        self.nethash = nethash
        self.version = version

    def accounts(self):
        return Account(self)

    def blocks(self):
        return Block(self)

    def delegates(self):
        return Delegate(self)

    def loaders(self):
        return Loader(self)

    def multiSignatures(self):
        return MultiSignature(self)

    def peers(self):
        return Peer(self)

    def signatures(self):
        return Signature(self)

    def transactions(self):
        return Transaction(self)

    def transports(self):
        return Transport(self)

    def votes(self):
        return Vote(self)

    def delegateBuilder(self):
        return DelegateBuilder(self)

    def multiSignatureBuilder(self):
        return MultiSignatureBuilder(self)

    def signatureBuilder(self):
        return SignatureBuilder(self)

    def transactionBuilder(self):
        return TransactionBuilder(self)

    def voteBuilder(self):
        return VoteBuilder(self)
