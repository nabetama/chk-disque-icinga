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


np.add_perfdata("used_memory_rate",           disque.used_memory)
np.add_perfdata("connected_clients",          disque.connected_clients)
np.add_perfdata("client_longest_output_list", disque.client_longest_output_list)
np.add_perfdata("client_biggest_input_buf",   disque.client_biggest_input_buf)
np.add_perfdata("client_biggest_input_buf",   disque.client_biggest_input_buf)
np.add_perfdata("rejected_connections",       disque.rejected_connections)
np.add_perfdata("total_commands_processed",   disque.total_commands_processed)
np.add_perfdata("total_connections_received", disque.total_connections_received)
np.add_perfdata("used_memory_human",          disque.used_memory_human)
np.add_perfdata("used_memory_peak_human",     disque.used_memory_peak_human)
np.add_perfdata("mem_fragmentation_ratio",    disque.mem_fragmentation_ratio)
np.add_perfdata("instantaneous_ops_per_sec",  disque.instantaneous_ops_per_sec)

code, messages = np.check_messages()

np.nagios_exit(
    code,
    messages,
)
    
