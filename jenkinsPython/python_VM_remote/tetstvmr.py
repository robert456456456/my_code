from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl

import argparse
import atexit
import sys
import ConfigParser

from pyVim import connect
 
__author__ = "Steve Jin"
path_vmn="\\\\nas\\Public\\QA\\Robert\\html\\python\\sh\\VMT\\Andrey\\LPO_Andrey.txt"
print path_vmn
VmName = open(path_vmn, "r").readlines()
temp = []
for x in VmName:
    x = x.replace("\n", "")
    temp.append(x)
vmnames = temp
print vmnames



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
if __name__ == "__main__":
    """demo/test code for the PyVmomi"""
 
    print "Starting to connect to ESXi ..."
    si = connect.Connect("192.168.1.220", 443, "qabot", "Vm512625!")
    content = si.content
    objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                        [vim.VirtualMachine],
                                                        True)
    vmList = objView.view
    objView.Destroy()
    print vmList
    print vim.VirtualMachine
   # Find the vm and power it on
    tasks = [vm.PowerOn() for vm in vmList if vm.name in vmnames]

      # Wait for power on to complete
    WaitForTasks(tasks, si)
    print "disconnecting to ESXi ..."
    connect.Disconnect(si)