import pysphere
import time
import ConfigParser
import sys
from os import path
from pysphere import VIServer

section = "Config"
for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
config = ConfigParser.RawConfigParser()
config.read(r'/nas/QA/Robert/html/python/cfg.ini')
delay = config.getint(section, 'interval')
loopCounter = config.getint(section, 'loop_count')
resource_pool1 = str(config.get(section, 'resource_pool'))
snapshot_name = str(config.get(section, 'snapshot_name'))
print snapshot_name
server_ip = str(config.get(section, 'server_ip'))
sever_login = str(config.get(section, 'sever_login'))
server_pw = str(config.get(section, 'server_pw'))
server = VIServer()


def remote(resource_poole, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw):
    server.connect(server_ip, sever_login, server_pw)
    vms = server.get_registered_vms(resource_pool=resource_poole)
    for x in range(0, len(vms)):
        vmz = server.get_vm_by_path(vms[x])
        status = vmz.get_status()
        if "POWERED OFF" in status and "CentOS" not in vms[x] and "ClearOS" not in vms[x]:
            try:
                vmz.revert_to_named_snapshot(snapshot_name)
                vmz.power_on()
                time.sleep(delay)
            except:
                print "with out snapshot: " + vms[x]


remote(resource_pool1, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw)
server.disconnect()
