from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl
import atexit
import sys
import ConfigParser
import time

section = "Short_Test_A"
for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
        print section
config = ConfigParser.RawConfigParser()
config.read('\\\\nas\\public\\QA\\Robert\\html\\python\\cfg.ini')
delay = config.getint(section, 'interval')
loopCounter = config.getint(section, 'loop_count')
#path_vnm = str(config.get(section, 'path_vmn'))
resource_pool1 = str(config.get(section, 'resource_pool'))
snapshot_name = str(config.get(section, 'snapshot_name'))
print snapshot_name
server_ip = str(config.get(section, 'server_ip'))
sever_login = str(config.get(section, 'sever_login'))
server_pw = str(config.get(section, 'server_pw'))
path_vmn ="\\\\nas\\Public\\QA\\Robert\\html\\python\\sh\\VMT\\Andrey\\LPO_Andrey.txt"
print path_vmn
VmName = open(path_vmn, "r").readlines()
temp = []
for x in VmName:
    x = x.replace("\n", "")
    temp.append(x)
VmName = temp
print VmName


def WaitForTasks(tasks, si):
   """
   Given the service instance si and tasks, it returns after all the
   tasks are complete
   """

   pc = si.content.propertyCollector

   taskList = [str(task) for task in tasks]

   # Create filter
   objSpecs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task)
                                                            for task in tasks]
   propSpec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task,
                                                         pathSet=[], all=True)
   filterSpec = vmodl.query.PropertyCollector.FilterSpec()
   filterSpec.objectSet = objSpecs
   filterSpec.propSet = [propSpec]
   filter = pc.CreateFilter(filterSpec, True)

   try:
      version, state = None, None

      # Loop looking for updates till the state moves to a completed state.
      while len(taskList):
         update = pc.WaitForUpdates(version)
         for filterSet in update.filterSet:
            for objSet in filterSet.objectSet:
               task = objSet.obj
               for change in objSet.changeSet:
                  if change.name == 'info':
                     state = change.val.state
                  elif change.name == 'info.state':
                     state = change.val
                  else:
                     continue

                  if not str(task) in taskList:
                     continue

                  if state == vim.TaskInfo.State.success:
                     # Remove task from taskList
                     taskList.remove(str(task))
                  elif state == vim.TaskInfo.State.error:
                     raise task.info.error
         # Move to next version
         version = update.version
   finally:
      if filter:
         filter.Destroy()
def conect():
    si = None
    try:
     si = SmartConnect(host='192.168.1.220',
                       user='qabot',
                       pwd='Vm512625!',
                       port=int('443'))
    except IOError, e:
     pass
    if not si:
     print "Cannot connect to specified host using specified username and password"
     sys.exit()


# Start program
def main():
   """
   Simple command-line program for powering on virtual machines on a system.
   """


   try:
      vmnames = VmName
      print vmnames
      if not len(vmnames):
         print "No virtual machine specified for poweron"
         sys.exit()


      '''
      try:
         si = SmartConnect(host='192.168.1.220',
                           user='qabot',
                           pwd='Vm512625!',
                           port=int('443'))
      except IOError, e:
         pass
      if not si:
         print "Cannot connect to specified host using specified username and password"
         sys.exit()
'''
      si=conect()
      atexit.register(Disconnect, si)

      # Retreive the list of Virtual Machines from the invetory objects
      # under the rootFolder
      content = si.content
      objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                        [vim.VirtualMachine],
                                                        True)
      vmList = objView.view
      objView.Destroy()

      # Find the vm and power it on
      for x in range(0, loopCounter):

             if vmnames[x] in VmName:
                try:
                   tasks = [vm.PowerOn() for vm in vmList if vm.name in vmnames[x]]
                   time.sleep(delay)
                except:
                     print "with out snapshot: " +vmnames[x]




      # Wait for power on to complete
      WaitForTasks(tasks, si)

      print "Virtual Machine(s) have been powered on successfully"
   except vmodl.MethodFault, e:
      print "Caught vmodl fault : " + e.msg
   except Exception, e:
      print "Caught Exception : " + str(e)

# Start program
if __name__ == "__main__":
   main()
