#!/usr/bin/python
# VMware vSphere Python SDK
# Copyright (c) 2008-2013 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Python program for listing the vms on an ESX / vCenter host
"""

from optparse import OptionParser, make_option
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vmodl
from time import sleep
from pyVmomi import vim


import atexit
import sys

vmlist = []
server_ip='192.168.1.220'
sever_login='qabot'
server_pw='Vm512625!'
def conect(server_ip, sever_login, server_pw):

         si = SmartConnect(host=server_ip,
                user=sever_login,
                pwd=server_pw,
                port=int('443'))

         return si

def PrintVmInfo(vm):
    """
    Print information for a particular virtual machine.
    """

    summary = vm.summary
    print "Name       : ", summary.config.name
    print "Path       : ", summary.config.vmPathName
    print "Guest      : ", summary.config.guestFullName
    annotation = summary.config.annotation
    if annotation != None and annotation != "":
        print "Annotation : ", annotation
    print "State      : ", summary.runtime.powerState
    if summary.guest != None:
        ip = summary.guest.ipAddress
        if ip != None and ip != "":
            print "IP         : ", ip
    if summary.runtime.question != None:
        print "Question  : ", summary.runtime.question.text
    print ""

def main():
    """
    Simple command-line program for listing the virtual machines on a system.
    """


    try:
        si = None
        try:
            si =conect(server_ip, sever_login, server_pw)
        except IOError, e:
            pass
        if not si:
            print "Could not connect to the specified host using specified username and password"
            return -1

        atexit.register(Disconnect, si)

        content = si.RetrieveContent()
        datacenter = content.rootFolder.childEntity[0]
        vmFolder = datacenter.vmFolder
        vmList = vmFolder.childEntity
        for vm in vmList:
            #PrintVmInfo(vm)
            if "[Office 6] Robert/" in vm.summary.config.vmPathName:
                vmlist.append(vm)
        for a in vmlist:
            #print a.summary.config.vmPathName
            PrintVmInfo(vm)

            if a.summary.runtime.powerState in 'poweredOff':

                  a.RevertToCurrentSnapshot()
                  a.PowerOn()
                  PrintVmInfo(vm)
            #print a.Snapshot
            #print a.refresh_snapshot_list()
            #print dir(a)
            #print a.RevertToCurrentSnapshot().info.name.info.__dict__

            #a.RevertToCurrentSnapshot().SetCustomValue(value="base 2", key=None)
            #a.GoToSnapshot()
            #print a
            #print dir(a)
            #a.snapshot(name="base 2")
            #print a.snapshot.rootSnapshotList.reverse()
            #print dir(a.snapshot.currentSnapshot.RevertToSnapshot_Task)
            #print dir(a.snapshot.rootSnapshotList.reverse)
           # print dir(a.snapshot)
            #print a.snapshot.currentSnapshot.config.name
            #print a.snapshot.currentSnapshot.childSnapshot.__dict__
            #a.snapshot.currentSnapshot.setCustomValue(value="base 2")
            print "=============================================================="
            #print a.__dict__
            #a.snapshot.rootSnapshotList.reverse()
            #a.snapshot.currentSnapshot.RevertToSnapshot_Task(value="base 2")
            #vim
            #a.snapshot('base 2')

            sleep(20)

    except vmodl.MethodFault, e:
        print "Caught vmodl fault : " + e.msg
        return -1
    except Exception, e:
        print "Caught exception : " + str(e)
        return -1

    return 0

# Start program
if __name__ == "__main__":
    main()
