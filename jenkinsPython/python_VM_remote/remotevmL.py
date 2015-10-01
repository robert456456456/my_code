import pysphere
import ConfigParser
import sys
import pysphere
import time
import ConfigParser
import sys
#section='base2'
section = "Config"
huynya = "[Office 6]"

for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
        print section
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
#ins = open("/nas/QA/Robert/html/python/VMN.txt", "r")
#VmName = []
#print VmName[0]
#for line in ins:
#    VmName.append(line)
#ins.close()
VmName = open("/nas/QA/Robert/html/python/VMN_Test.txt", "r").readlines()
#VmName = ['7 Ultimate x64 sp1 Office6 Andrey','7 Ultimate x86 sp0 office6 Andrey','8 Pro x64 sp0 Office6 Andrey','8.1 final x86 Office6 Andrey','7 Ultimate x64 sp0 Office6 Andrey','7 Ultimate x86 sp1 office6 Andrey','8 Pro x86 sp0 Office6 Andrey']
print VmName
temp = []
for x in VmName:
    x = x.replace("\n", "")
    temp.append(x)
VmName = temp
#print VmName
def remote(resource_poole, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw):
    #201
    server.connect(server_ip, sever_login, server_pw)
    #resource_pool="/Resources/Robert"
    vms = server.get_registered_vms(resource_pool=resource_poole)
    #loopCounter=51
    #delay=10
    count1 = 0
    for x in range(0, loopCounter):
        vmz = server.get_vm_by_path(vms[x])
        #print x
        #print "vms[x]:" + vms[x]
        status = vmz.get_status()
        #print count1
        #print "bob"
        #print VmName[count1]
        #print "bobert"

        if vms[x] in VmName:
            #print 'bob'
            count1 += 1
            try:
                vmz.revert_to_named_snapshot(snapshot_name)
                vmz.power_on()
            except:
                print "with out snapshot: " + vms[x]
        time.sleep(delay)


remote(resource_pool1, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw)
server.disconnect()
