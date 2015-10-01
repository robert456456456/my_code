from xml.dom import minidom
import json
from pprint import pprint
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl
import atexit
import sys
import ConfigParser
import collections
import time

import traceback

section = "Config"
for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
        print section

config = ConfigParser.RawConfigParser()
config.read(r'/nas/QA/Robert/html/python/cfg.ini')
delay = config.getint(section, 'interval')
loopCounter = config.getint(section, 'loop_count')
path_vnm = str(config.get(section, 'path_vmn'))
Count_vm = str(config.get(section, 'count_vm'))
resource_pool1 = str(config.get(section, 'resource_pool'))
snapshot_name = str(config.get(section, 'snapshot_name'))
server_ip = str(config.get(section, 'server_ip'))
sever_login = str(config.get(section, 'sever_login'))
server_pw = str(config.get(section, 'server_pw'))
fxml1 = str(config.get(section, 'xml_pro'))
fjson1 = str(config.get(section, 'json_pro'))
fxml2 = str(config.get(section, 'old_xml'))
fjson2= str(config.get(section, 'old_json'))
path_vnm_m= str(config.get(section, 'path_vmn_m'))
countVM = open(Count_vm, "r").read()

countVM = int(countVM)
VmName = open(path_vnm, "r").readlines()
temp = []
arr1= []
arr2= []
for x in VmName:
    x = x.replace("\n", "")
    temp.append(x)
VmName = temp

#fxml1= '//nas/Public/QA/Robert/html/AutoHotkey_bot_ie11/forQA/Teapot/andrey/example.xml'
#fjson1= '//nas/Public/QA/Robert/html/AutoHotkey_bot_ie11/forQA/Teapot/andrey/example.json'
#fxml2= '//nas/Public/QA/Robert/html/AutoHotkey_bot_ie11/forQA/Teapot/andrey/example1.xml'
#fjson2= '//nas/Public/QA/Robert/html/AutoHotkey_bot_ie11/forQA/Teapot/andrey/example1.json'

class Tipot_vm:
    def __init__(self):
        pass
    def start(self):

         self.arr1 = self.get_m(fxml1, fjson1)
         self.arr2 = self.get_m(fxml2, fjson2)
         for av, result in self.sameerence(self.arr1,self.arr2):
                av = av.strip()
                result = result.strip()
                print av

         self.remote(delay, server_ip, sever_login, server_pw,av)




    def parse_element(self, element):
        dict_data = dict()
        if element.nodeType == element.TEXT_NODE:
            dict_data['data'] = element.data
        if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_NODE,
                                    element.DOCUMENT_TYPE_NODE]:
            for item in element.attributes.items():
                dict_data[item[0]] = item[1]
        if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_TYPE_NODE]:
            for child in element.childNodes:
                child_name, child_dict = self.parse_element(child)
                if child_name in dict_data:
                    try:
                        dict_data[child_name].append(child_dict)
                    except AttributeError:
                        dict_data[child_name] = [dict_data[child_name], child_dict]
                else:
                    dict_data[child_name] = child_dict
        return element.nodeName, dict_data


    def pars(self,mashin,fxml,fjson ):
        dom = minidom.parse(fxml)
        f = open(fjson, 'w')
        f.write(json.dumps(self.parse_element(dom), sort_keys=True, indent=4))
        f.close()
        json_data = open(fjson).read()
        data = json.loads(json_data)
        #pprint(data)
        x = data[1]
        machine = ''
        for b, z in x.items():
            for item, item2 in z.items():
                if item == mashin:
                    machine += item
                    machine_num = machine.split("_")[-1]
                    if len(machine_num) < 2:
                        item23 = 'A00' + machine_num + 'A'
                    else:
                        item23 = 'A0' + machine_num + 'A'
                        #print item2
                    for item3, item4 in item2.items():
                        for item5, item6 in item4.items():
                           return item23, item6

    def difference(self,array1, array2):
            """

            :param array1:
            :param array2:
            :return:
            """
            array = []
            for x in array2:
                if x not in array1:
                    array.append(x)
            # print array
            return array
    def sameerence(self, array1, array2):
            """

            :param array1:
            :param array2:
            :return:
            """
            array = []
            for x in array2:
                if x in array1:
                    array.append(x)
            # print array
            return array

    def get_m(self,fxml,fjson):
        path_vnm_1 = path_vnm_m
        VmName_1 = open(path_vnm_1, "r").readlines()
        temp_1 = []
        bob= []
        for x in VmName_1:
            x = x.replace("\n", "")
            temp_1.append(x)
        VmName_1 = temp_1
        for z1 in range(0, len(VmName_1)):
           b = self.pars(VmName_1[z1],fxml,fjson)
           bob.append(b)
        return bob
            #print VmName[z1]

    def conect(self,server_ip, sever_login, server_pw):
        si = SmartConnect(host=server_ip,
                          user=sever_login,
                          pwd=server_pw,
                          port=int('443'))

        return si
    def remote(self, delay, server_ip, sever_login, server_pw,vm_list):

       try:

          if not len(vm_list):
             print "No virtual machine specified for poweron"
             sys.exit()

          si = None
          try:
             si =self.conect(server_ip, sever_login, server_pw)
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
                  if vm.name in vm_list[x] and vm.runtime.powerState in 'poweredOn':
                      try:
                         #vm.RevertToCurrentSnapshot()
                         #vm.PowerOn()
                         print vm_list[x]
                         time.sleep(delay)
                      except:
                           print "with out snapshot: " +vm_list[x]
          print "Virtual Machine(s) have been powered on successfully"
       except vmodl.MethodFault, e:
          print "Caught vmodl fault : " + e.msg
       except Exception, e:
          print "Caught Exception : " + str(e)




    def remote_count(self,resource_poole, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw, path_vmn, defi):
        """
       Simple command-line program for powering on virtual machines on a system.
       """

        try:
            if not len(VmName):
                print "No virtual machine specified for poweron"
                sys.exit()

            si = None
            try:
                si = self.conect(server_ip, sever_login, server_pw)
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
            #print len(vmList)
            # Find the vm and power it on
            count=0
            for x in range(0, len(vmList)):

                for vm in vmList:
                    if vm.name in VmName[x] and vm.runtime.powerState in 'poweredOff' and count < defi:

                        try:

                            #print 'bob'
                            count = count+1
                            #print count
                            #vm.RevertToCurrentSnapshot()
                            vm.PowerOn()
                            time.sleep(delay)
                        except:

                            #collections.Counter(vm.name in VmName[x] and vm.runtime.powerState in 'poweredOn')
                            print "with out snapshot: " + VmName[x]

            print "Virtual Machine(s) have been powered on successfully"
        except vmodl.MethodFault, e:
            print "Caught vmodl fault : " + e.msg
        except Exception, e:
            print "Caught Exception : " + str(e)


    def count_vm(self,server_ip, sever_login, server_pw, status):
        """
       Simple command-line program for powering on virtual machines on a system.
               """

        try:
            if not len(VmName):
                print "No virtual machine specified for poweron"
                sys.exit()

            si = None
            try:
                si = self.conect(server_ip, sever_login, server_pw)
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
            #print len(vmList)
            # Find the vm and power it on
            c = 0
            for x in range(0, len(vmList)):
                for vm in vmList:
                    if vm.name in VmName[x] and vm.runtime.powerState in status:

                        try:
                            c = c + 1
                        except:
                            print "with out snapshot: " + VmName[x]

            print "Virtual Machine(s) have been powered on successfully"
        except vmodl.MethodFault, e:
            print "Caught vmodl fault : " + e.msg
        except Exception, e:
            print "Caught Exception : " + str(e)
            #print c
            return c


    def count_pwon(self,runvmcount1, runvmcount2):
        runvmcount = runvmcount1 - runvmcount2
        if runvmcount == 0 or runvmcount < 0:
            runvmcount = -1
            #print runvmcount
            return runvmcount
        else:
            #print runvmcount
            return runvmcount

    def main(self):
        status = 'poweredOn'
        runvmcount2 = self.count_vm(server_ip, sever_login, server_pw, status)
        runvmcount1 = countVM
        defi=self.count_pwon(runvmcount1, runvmcount2)
        if defi == -1:
            print 'not vm to poweON'
        else:
          self.remote_count(resource_pool1, snapshot_name, loopCounter, delay, server_ip, sever_login, server_pw, path_vnm, defi)


''''
arr1 = Tipot_vm.get_m(fxml1, fjson1)
arr2 = Tipot_vm.get_m(fxml2, fjson2)
#print difference(arr1,arr2)
for av, result in Tipot_vm.sameerence(arr11,arr2):
        av = av.strip()
        result = result.strip()
        print av

#pars('number_machine_32')
'''
scanner = Tipot_vm()
scanner.start()