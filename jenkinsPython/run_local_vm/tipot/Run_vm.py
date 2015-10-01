'''
Created on jun 23, 2014

@author: Robert Adinihy
'''
__author__ = 'Robert Adinihy'
import os
import time
print(os.system('D:\\qa-automation\\jenkinsPython\\run_local_vm\\vm_status.sh'))
f = open('D:\\qa-automation\\jenkinsPython\\run_local_vm\\status.txt', 'r')
print f.read()
bob = f.read()
for x in range(0, 450):
    if bob in 'Total running VMs: 0':
        try:
            #os.system('D:\\qa-automation\\jenkinsPython\\run_local_vm\\revert_snap_powerOn.sh')
            os.system('D:\\qa-automation\\jenkinsPython\\run_local_vm\\revert_snap_powerOn_e.sh')
            time.sleep(120)
            os.system('D:\\qa-automation\\jenkinsPython\\run_local_vm\\vm_status.sh')
            bob = f.read()
        except:
            print "end test "