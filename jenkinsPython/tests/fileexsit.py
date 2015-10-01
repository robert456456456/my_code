#!/usr/bin/python
import os

IE8="Milishes_IE8"
IE9="Milishes_IE9"
IE10="Milishes_IE10"
py="python /nas/QA/Robert/html/python/remotevm.py section="
p1="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE11.txt"
p2="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE19.txt"
p3="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE10.txt"
if os.path.isfile(p1): 
   os.system(py+IE8) 
print "file does exist at this time"
elif os.path.isfile(p2):
  os.system(py+IE9) 
 
elif os.path.isfile(p3):	    
 os.system(py+IE10)
