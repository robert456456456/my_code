import pysphere
import time
from pysphere import VIServer
server = VIServer()
server.connect('192.168.1.220','qabot','Vm512625!')

def server_performance(ip, mem_usage, cpu_usage):
    hosts = server.get_hosts()
    pm = server.get_performance_manager()
    block = True
    while(block):
        for h in hosts:
            if hosts[h] == ip:
                time.sleep(10)
                mem = pm.get_entity_statistic(h, ['mem.usage'])[0].value
                mem = int(mem)
                cpu = pm.get_entity_statistic(h, ['cpu.usage'])[0].value
                cpu = int(cpu)
                if mem < mem_usage and cpu < cpu_usage:
                    block = False
                    print 'false'



server.disconnect()
server_performance('192.168.1.200','30','30')