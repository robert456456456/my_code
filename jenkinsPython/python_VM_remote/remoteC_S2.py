__author__ = 'Robert Adinihy'
import datetime
import MySQLdb
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
        #print section
    if x[0:10] == 'test_name=':
        test_name1 = x[10::]

config = ConfigParser.RawConfigParser()
config.read(r'/nas/QA/Robert/html/python/cfg.ini')
delay = config.getint(section, 'interval')
server_ip = str(config.get(section, 'server_ip'))
sever_login = str(config.get(section, 'sever_login'))
server_pw = str(config.get(section, 'server_pw'))
db_ip = str(config.get(section, 'db_ip'))
db_name = str(config.get(section, 'db_name'))
db_user = str(config.get(section, 'db_user'))
db_pw = str(config.get(section, 'db_pw'))
db = MySQLdb.connect(host=db_ip, user=db_user, passwd=db_pw, db=db_name)
cur = db.cursor()
test_name = test_name1
bob = []
print test_name
cur.execute("SELECT id FROM test where `Name` = '" + test_name + "' and `Type` = 'Test'")

for row in cur.fetchall():
 tests_id = row[0]
try:
    sql_rec="SELECT vm_name, snap_name FROM vm_tests where test_id = " + str(tests_id) + " "'ORDER BY vm_tests.vm_name ASC'";"
    cur.execute(sql_rec)
    for row in cur.fetchall():
     bob.append(row[0])
    VmName =bob
    print VmName
except MySQLdb.Error, e:
 print "An error has been passed. %s" %e
def conect(server_ip, sever_login, server_pw):

         si = SmartConnect(host=server_ip,
                user=sever_login,
                pwd=server_pw,
                port=int('443'))

         return si
def remote(delay, server_ip, sever_login, server_pw):
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
                    #print row[1]
                    r = requests.get("http://192.168.0.14:7777/?Command=Create_Snapshot&vm_name=" + VmName[x]+"&snapshot_name=" +row[1])
                    #print "http://192.168.0.14:7777/?Command=Create_Snapshot&vm_name=" + VmName[x]+"&snapshot_name=" +row[1]
                    r.text
                  except:
                       print "with out snapshot: " +VmName[x]
      print "Virtual Machine(s) have been powered on successfully"
   except vmodl.MethodFault, e:
      print "Caught vmodl fault : " + e.msg
   except Exception, e:
      print "Caught Exception : " + str(e)







remote(delay, server_ip, sever_login, server_pw)

