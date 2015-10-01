import pysphere
import time
import ConfigParser
import sys
#section='base2'
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
resource_pool1 = str(config.get(section, 'resource_pool'))
snapshot_name = str(config.get(section, 'snapshot_name'))
path_vmn = str(config.get(section, 'path_vmn'))
print snapshot_name
server_ip = str(config.get(section, 'server_ip'))
sever_login = str(config.get(section, 'sever_login'))
server_pw = str(config.get(section, 'server_pw'))
server = VIServer()
def remote(resource_poole, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw,path_vmn):
    server.connect(server_ip, sever_login, server_pw)
    vms = server.get_registered_vms(resource_pool=resource_poole)
    print resource_poole
    print vms
    for x in range(0, len(vms)):

        print x
        print "vms[x]:" + vms[x]
        time.sleep(delay)
        f = open(path_vmn, "a")
        f.write(vms[x] + '\n')
        time.sleep(delay)


remote(resource_pool1, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw, path_vmn)
server.disconnect()
