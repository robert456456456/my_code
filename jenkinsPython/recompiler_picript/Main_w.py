__author__ = 'Robert Adinihy '

import Wcompiler_op

import Constans
import sys
W_object = Wcompiler_op.op()
section = ""
for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
        break
print section
if section == 'BHO':
    W_object.get_des_location(Constans.W_dest_BHO,Constans.BHO_bat_l,Constans.Ootput_txt_BHO,Constans.Output_location_W)
elif section == 'BHO_un':
    W_object.get_des_location(Constans.W_dest_BHO_un,Constans.BHO_bat_l,Constans.Ootput_txt_BHO_un,Constans.Output_location_W_un)
elif section == 'Bijo':
     W_object.get_des_location(Constans.W_dest_Bijo,Constans.BHO_bat_l,Constans.Ootput_txt_BHO,Constans.Output_location_W)
elif section == 'BHO_M':
    W_object.muve_f(Constans.W_dest_BHO,Constans.M_W_dest_BHO)
elif section == 'BHO_un_M':
    W_object.muve_f(Constans.W_dest_BHO_un,Constans.M_W_dest_BHO_un)
elif section == 'Bijo_M':
     W_object.muve_f(Constans.W_dest_Bijo,Constans.M_W_dest_Bijo)



else:
    print 'no section be choes'
#elif section == 'chrome_32':
    #old_checker_pro.Builder_checker().chrome_silicon_32()
#elif section == 'chrome_64':
    #old_checker_pro.Builder_checker().chrome_sillicon_64()
#elif section == 'FF_S':
    #old_checker_pro.Builder_checker().ff_silicon_pro()
