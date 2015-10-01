import pysphere
import time
import ConfigParser
import sys
#section='bob'
section = "Config"

for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]

from os import path
from pysphere import VIServer

config = ConfigParser.RawConfigParser()
config.read(r'/nas/QA/Robert/html/python/cfg.ini')
delay = config.getint(section, 'interval') #interval in seconds
loopCounter = config.getint(section, 'loop_count')
resource_pool1 = str(config.get(section, 'resource_pool'))
snapshot_name = str(config.get(section, 'snapshot_name'))
print snapshot_name
server_ip = str(config.get(section, 'server_ip'))
sever_login = str(config.get(section, 'sever_login'))
server_pw = str(config.get(section, 'server_pw'))
server = VIServer()


def remote(resource_poole, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw):
    #201
    server.connect(server_ip, sever_login, server_pw)
    #resource_pool="/Resources/Robert"
    vms = server.get_registered_vms(resource_pool=resource_poole)
    #loopCounter=51
    #delay=10
    for x in range(0, loopCounter):
        vmz = server.get_vm_by_path(vms[x])
        status = vmz.get_status()
        if "POWERED OFF" in status:
            if "CentOS" not in vms[x]:
                if "ClearOS" not in vms[x]:
                    if "7 Ultimate x64 sp1 McAfee-GW-Edition" not in vms[x]:
                        if "7 Ultimate x64 sp1 TrendMicro-HouseCal" not in vms[x]:
                            if "7 Ultimate x64 sp1 360" not in vms[x]:
                                if "7 Ultimate x64 sp1 ByteHero" not in vms[x]:
                                    if "7 Ultimate x64 sp1 Commtouch" not in vms[x]:
                                        if "7 Ultimate x64 sp1 eSafe" not in vms[x]:
                                            if "7 Ultimate x64 sp1 Jiangmin" not in vms[x]:
                                                if "7 Ultimate x64 sp1 Jin Shan" not in vms[x]:
                                                    if "7 Ultimate x64 sp1 Kaba 365" not in vms[x]:
                                                        if "7 Ultimate x64 sp1 MicroWorld-eScan" not in vms[x]:
                                                           if "7 Ultimate x64 sp1 Qianyun" not in vms[x]:
                                                              if "7 Ultimate x64 sp1 The Hacker" not in vms[x]:
                                                                  if "7 Ultimate x64 sp1 VBA32" not in vms[x]:
                                                                     if "7 Ultimate x64 sp1 VirusBuster" not in vms[x]:
                                                                        try:
                                                                            #text =  vms[x]
                                                                            #vmz.delete_named_snapshot(snapshot_name, sync_run=False)
                                                                            vmz.create_snapshot(snapshot_name)
                                                                            print "with snapshot: " + vms[x]

                                                                        except:
                                                                          print "with out snapshot: " + vms[x]
                                                    time.sleep(delay)


remote(resource_pool1, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw)
server.disconnect()