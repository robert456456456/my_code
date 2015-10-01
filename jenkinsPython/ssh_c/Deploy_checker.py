__author__ = 'Robert Adinihy '

import ssh_c
import sys
import Constans
shh = ssh_c.Builder_compiler()

section = ""
for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
        break
print section
if section == Constans.brand_c_i:
    shh.costrator_Al_I(Constans.brand_c_i)

elif section == Constans.brand_c_bi:
    shh.costrator_Al(Constans.brand_c_bi)

elif section == Constans.brand_c_bh:
    print Constans.brand_c_bh
    shh.costrator_Al(Constans.brand_c_bh)

elif section == Constans.brand_c_un:
   shh.costrator_Al(Constans.brand_c_un)

elif section == Constans.brand_c_ff:
    shh.costrator_Al(Constans.brand_c_ff)

elif section == Constans.brand_c_al:
    shh.costrator_Al(Constans.brand_c_al)

else:

 print "section doesn't exsit"





