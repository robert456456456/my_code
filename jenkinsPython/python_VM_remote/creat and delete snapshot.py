import pysphere
import time
import ConfigParser
import sys
#section='bob'
section="Config"

for x in sys.argv:
	if x[0:8] == 'section=':
		section=x[8::]

from os import path
from pysphere import VIServer
config = ConfigParser.RawConfigParser()
config.read(r'/nas/QA/Robert/html/python/cfg.ini')
delay = config.getint(section, 'interval') #interval in seconds
loopCounter=config.getint(section, 'loop_count')
resource_pool1= str(config.get(section, 'resource_pool'))
snapshot_name= str(config.get(section, 'snapshot_name'))
print snapshot_name
server_ip= str(config.get(section, 'server_ip'))
sever_login= str(config.get(section, 'sever_login'))
server_pw= str(config.get(section, 'server_pw'))

server=VIServer()
def crete_deleteS(resource_poole,snapshot_name,loopCounter,delay,server_ip,sever_login,server_pw):
	server.connect(server_ip,sever_login,server_pw)
	#resource_pool="/Resources/Robert"
	vms=server.get_registered_vms(resource_pool=resource_poole)

	file=open('testlog.txt','r')
	for i in range(0,loopCounter):
		line=file.readline()
		if "Done" in line :
			newline=line.replace(" Done\n","")
			vmz=server.get_vm_by_path(newline)
			vmz.power_off()
			vmz.delete_named_snapshot(snapshot_name)
			vmz.create_snapshot(snapshot_name)
		else:
			print line + "was up and I could not touch it"
			time.sleep(delay)
crete_deleteS(resource_poole1,snapshot_name,loopCounter,delay,server_ip,sever_login,server_pw)
server.disconnect()