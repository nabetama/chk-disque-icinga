# coding: utf-8

from pydisque.client import Client
from pynag.Plugins import WARNING, CRITICAL, OK, UNKNOWN, simple as Plugin

client = Client()
client.connect()

np = Plugin()
np.activate()


class Disque(object):
    def __init__(self):
        self.__info = client.execute_command('INFO')
        self.create_prop()

    def create_prop(self):
        for k, v in self.__info.iteritems():
            self.__dict__[k] = v

disque = Disque()


np.add_perfdata("used_memory_rate",           disque.used_memory)
np.add_perfdata("connected_clients",          disque.conncted_clients)
np.add_perfdata("client_longest_output_list", disque.client_longest_output_list)
np.add_perfdata("cient_biggest_input_buf",    disque.cient_biggest_input_buf)
np.add_perfdata("cient_biggest_input_buf",    disque.cient_biggest_input_buf)
np.add_perfdata("rejected_connections",       disque.rejected_connections)
np.add_perfdata("total_commands_processed",   disque.total_commands_processed)
np.add_perfdata("total_connections_received", disque.total_connections_received)
np.add_perfdata("used_memory_human",          disque.info.used_memory_human)
np.add_perfdata("used_memory_human",          disque.info.used_memory_human)
np.add_perfdata("used_memory_peak_human",     disque.used_memory_peak_human)
np.add_perfdata("mem_fragmentation_ratio",    disque.mem_fragmentation_ratio)
np.add_perfdata("instantaneous_ops_per_sec",, disque.instantaneous_ops_per_sec)
