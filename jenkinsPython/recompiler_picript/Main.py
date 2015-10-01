__author__ = 'Robert Adinihy '

import Wcompiler_op
import jenkins_log
import Constans
import sys
W_object = Wcompiler_op.op()
J_object = jenkins_log.jenkins_log()
section = ""
for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
        break
print section
if section == 'BHO_j':
    J_object.conection_run_comand(Constans.QA_Builder_url,Constans.port,Constans.user,Constans.pw,Constans.comand_i)
    J_object.clear(Constans.Output_location)
    J_object.location(Constans.Main_location_bho,Constans.Sub_loction_BHO1,Constans.Output_location)
    J_object.location(Constans.Main_location_bho,Constans.Sub_loction_BHO2,Constans.Output_location)
elif section == 'BHO_u':
    J_object.conection_run_comand(Constans.QA_Builder_url,Constans.port,Constans.user,Constans.pw,Constans.comand_i_un)
    J_object.clear(Constans.Output_location_un)
    J_object.location(Constans.Main_location_bho_un,Constans.Sub_loction_BHO_un,Constans.Output_location_un)
elif section == 'Bijo':
    J_object.conection_run_comand(Constans.QA_Builder_url,Constans.port,Constans.user,Constans.pw,Constans.comand_i2)
    J_object.clear(Constans.Output_location)
    J_object.location(Constans.Main_location_bho,Constans.Sub_loction_BHO1,Constans.Output_location)
    J_object.location(Constans.Main_location_bho,Constans.Sub_loction_BHO2,Constans.Output_location)
else:
    print 'no section be choes'
#elif section == 'chrome_32':
    #old_checker_pro.Builder_checker().chrome_silicon_32()
#elif section == 'chrome_64':
    #old_checker_pro.Builder_checker().chrome_sillicon_64()
#elif section == 'FF_S':
    #old_checker_pro.Builder_checker().ff_silicon_pro()

