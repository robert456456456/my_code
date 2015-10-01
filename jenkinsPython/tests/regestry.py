'''
Created on Nov 5, 2013

@author: robert
'''
#!/usr/bin/python
from _winreg import *


aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProductName")
for i in range(1024):
    try:
        #print Enumkey(aKey,i)
        asubkey_name=EnumKey(aKey,i)
        asubkey=OpenKey(aKey,asubkey_name)
        print asubkey_name
        val=QueryValueEx(asubkey, "DisplayName")
        if val[0][0:3] != "CCC":
            print val[0]
    except:
        pass  