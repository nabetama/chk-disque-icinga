#!/usr/bin/env python
# coding: utf-8

import sys
from pydisque.client import Client
from pynag.Plugins import CRITICAL, simple as Plugin


np = Plugin(must_threshold=False)
np.activate()


try:
    client = Client()   # Client(['127.0.0.1:7711'])
    client.connect()
except:
    np.nagios_exit(
        CRITICAL,
        'Mayby disque is down.',
    )
    sys.exit(1)

class Disque(object):
    def __init__(self):
        self.__info = client.execute_command('INFO')
        self.create_properties()

    def create_properties(self):
        for k, v in self.__info.iteritems():
            self.__dict__[k] = v

disque = Disque()

info_properties = [
    "used_memory_rate",
    "connected_clients",
    "client_longest_output_list",
    "client_biggest_input_buf",
    "client_biggest_input_buf",
    "rejected_connections",
    "total_commands_processed",
    "total_connections_received",
    "used_memory_human",
    "used_memory_peak_human",
    "mem_fragmentation_ratio",
    "instantaneous_ops_per_sec",
]

for info_property in info_properties:
    np.add_perfdata(info_propert, getattr(disque, info_property))

code, messages = np.check_messages()

np.nagios_exit(
    code,
    messages,
)

