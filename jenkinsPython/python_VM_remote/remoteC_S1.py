from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl
import atexit
import sys
import ConfigParser
import time
import requests

import traceback
section = "Config"
for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
    if x[0:5] == 'snap=':
        snap = x[5::]
        print snap
        #print section

config = ConfigParser.RawConfigParser()
config.read(r'/nas/QA/Robert/html/python/cfg.ini')
delay = config.getint(section, 'interval')###vm start intervall 
loopCounter = config.getint(section, 'loop_count')
path_vnm = str(config.get(section, 'path_vmn'))
resource_pool1 = str(config.get(section, 'resource_pool'))
snapshot_name = str(config.get(section, 'snapshot_name')) ### array vms snap name
#print snapshot_name
server_ip = str(config.get(section, 'server_ip'))
sever_login = str(config.get(section, 'sever_login'))
server_pw = str(config.get(section, 'server_pw'))
#print path_vnm
VmName = open(path_vnm, "r").readlines() ### array vms name
temp = []
for x in VmName:
    x = x.replace("\n", "")
    temp.append(x)
VmName = temp
print temp
def conect(server_ip, sever_login, server_pw):

         si = SmartConnect(host=server_ip,
                user=sever_login,
                pwd=server_pw,
                port=int('443'))

         return si
def remote(resource_poole, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw,path_vmn):
   """
   Simple command-line program for powering on virtual machines on a system.
   """


   try:
      if not len(VmName):
         print "No virtual machine specified for poweron"
         sys.exit()

      si = None
      try:
         si =conect(server_ip, sever_login, server_pw)
      except IOError, e:
         pass
      if not si:
         print "Cannot connect to specified host using specified username and password"
         sys.exit()

      atexit.register(Disconnect, si)
      content = si.content
      objView = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
      vmList = objView.view
      objView.Destroy()
      print len(vmList)
      # Find the vm and power it on
      for x in range(0, len(vmList)):
          for vm in vmList:
              if vm.name in VmName[x] and vm.runtime.powerState in 'poweredOff':
                  try:
                    print VmName[x]
                    r = requests.get("http://192.168.0.14:7777/?Command=Create_Snapshot&vm_name=" + VmName[x]+"&snapshot_name=" +snap)
                    #print "http://192.168.0.14:7777/?Command=Create_Snapshot&vm_name=" + VmName[x]+"&snapshot_name=" +snap
                    r.text
                  except:
                       print "with out snapshot: " +VmName[x]
      print "Virtual Machine(s) have been powered on successfully"
   except vmodl.MethodFault, e:
      print "Caught vmodl fault : " + e.msg
   except Exception, e:
      print "Caught Exception : " + str(e)







remote(resource_pool1, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw, path_vnm)

