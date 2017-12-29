#!/usr/bin/env python

import os
import argparse
import sys

try:
    import json
except ImportError:
    import simplejson as json


class OurInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # This section is called with `--list`.
        if self.args.list:
            self.inventory = self.our_inventory()
        # this section is called with `--host [hostname]`.
        elif self.args.host:
            # We return _meta info `--list` so not complete.
            self.inventory = self.empty_inventory()

        # No vars or group? Return as an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print json.dumps(self.inventory);

    # This is an example used simply for testing and so we can run a dymanic script without actualy setting up a server
    # 

    def our_inventory(self):
        return {
            'group': {
                'hosts': ['spyton2.mylabserver.com', 'spyton3.mylabserver.com', 'spyton4.mylabserver.com'],
                'vars': {
                    'ansible_user': 'user',
                    'test_variable': 'nonspecific_value'
                }
            },
            '_meta': {
                'hostvars': {
                    'spyton2.mylabserver.com': {
                        'logs_folder': '/var/log'
                    },
                    'spyton3.mylabserver.com': {
                        'logs_folder': '/var/log2'
                    }
                }
            }
        }

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Lets take the args passed to us via the command line.

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
OurInventory()
