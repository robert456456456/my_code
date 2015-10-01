
import time
import ConfigParser
import sys
section = "Config"
for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
        print section
from os import path
from pysphere import VIServer
config = ConfigParser.RawConfigParser()
config.read(r'/nas/QA/Robert/html/python/cfg.ini')
delay = config.getint(section, 'interval')
loopCounter = config.getint(section, 'loop_count')
path_vnm = str(config.get(section, 'path_vmn'))
resource_pool1 = str(config.get(section, 'resource_pool'))
snapshot_name = str(config.get(section, 'snapshot_name'))
print snapshot_name
server_ip = str(config.get(section, 'server_ip'))
sever_login = str(config.get(section, 'sever_login'))
server_pw = str(config.get(section, 'server_pw'))
server = VIServer()
def remote(resource_poole, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw,path_vmn):
   # path_vmn="/nas/QA/Robert/html/python/VMN_LPO.txt"
    VmName = open(path_vmn, "r").readlines()
    temp = []
    for x in VmName:
        x = x.replace("\n", "")
        temp.append(x)
    VmName = temp
    print VmName
    server.connect(server_ip, sever_login, server_pw)
    vms = server.get_registered_vms(resource_pool=resource_poole)
    for x in range(0, len(vms)):


             status=vmz.get_status()
             vmz = server.get_vm_by_path(vms[x])
             if vms[x] in VmName and "POWERED OFF" in status:
                try:
                    vmz.revert_to_named_snapshot(snapshot_name)
                    vmz.power_on()
                    time.sleep(delay)
                except:
                     print "with out snapshot: " + vms[x]

remote(resource_pool1, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw, path_vnm)
server.disconnect()
