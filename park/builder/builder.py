#!/usr/bin/env python

from abc import ABC
from Naked.toolshed.shell import muterun_js
from jinja2 import Environment, FileSystemLoader
import sys
import json
import os


class Builder(ABC):
    def __init__(self, client):
        self.client = client
        self.env = Environment(
            loader=FileSystemLoader(
                os.path.join(os.path.dirname(__file__), 'templates')))

    def build(self, script, data):
        network = {
            '6e84d08bd299ed97c212c886c98a57e36545c8f5d645ca7eeae63a8bd62d8988':
            {"netPubKey":"0x17", 'js': 'arkjs'},  # ark mainnet
            '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23':
            {"netPubKey":"0x1E", 'js': 'arkjs'},  # ark devnet
            '313ea34c8eb705f79e7bc298b788417ff3f7116c9596f5c9875e769ee2f4ede1':
            {"netPubKey":"0x2D", 'js': 'arkjs'}, # kapu mainnet
            'f1ef11be7a879671b3019a785c9a2c9dbd9d800b05644d26ad132275ffe2dd48':
            {"netPubKey":"0x50", 'js': 'arkjs'}, # kapu devnet
            'b4e87739ca85f7eabf844a643930573e9a2dd9da291662e74d26962b5c3f0ed9':
            {"netPubKey":"0x42", 'js': 'persona-js'},  # persona testnet
            'bee1634649fc6a759e5fdb8f3c4bcb4b5189c1f2a6b48284a6445f3f09db844e':
            {"netPubKey":"0x37", 'js': 'ripajs'},  # ripa mainnet
            '14b55c1de06caa015362d59ad97a144bc3c9fc2b50ece84b78d13ceaeaf7d8fb':
            {"netPubKey":"0x37", 'js': 'persona-js'}  # persona mainnet
        }[self.client.nethash]

        template = self.env.get_template(script + ".py").render({
            **{
                "network": network['netPubKey'],
                "javascript": network['js']
            },
            **data
        })

        transactionScript = script + ".js"

        with open(transactionScript, "wt") as fh:
            fh.write(template)

        response = muterun_js(transactionScript)

        if response.exitcode == 0:
            os.remove(transactionScript)

            return json.loads(response.stdout.decode('utf-8'))
        else:
            sys.stderr.write(response.stderr.decode('utf-8'))
