__author__ = 'Robert adinhy'
#server Compilert
QA_Builder_url = "192.168.1.240"
port= 27628
user="root"
pw= 'Go512625'
##############################################################################################################################
#BHO
Main_location_bho='/tmp/Main.txt'
Sub_loction_BHO1="\\publish\\tools"
Sub_loction_BHO2="\\publish\\Installer.Release.Minimal"

Output_location='/nas/QA/Robert/mediy/Output.txt'
W_dest_BHO="c:\\BHO"
W_dest_Bijo="c:\\Bijo"
W_dest_BHO_un="c:\\BHO_un"
M_W_dest_BHO="d:\\BHO"
M_W_dest_Bijo="d:\\Bijo"
M_W_dest_BHO_un="d:\\BHO_un"
W_sub_BHO="tlb"
BHO_bat_l = "c:\\BHO_bat\\"
Ootput_txt_BHO = 'test.txt'
extention_b='.bat'
Output_location_W="\\\\nas\\public\\QA\\Robert\\mediy\\Output.txt"

#Comands
comand_i='cat /var/lib/jenkins/jobs/BHO_Builder/lastSuccessful/log|grep "Copy to"|cut -d " " -f 3 >'+Main_location_bho
comand_i2='cat /var/lib/jenkins/jobs/Bijo_Builder/lastSuccessful/log|grep "Copy to"|cut -d " " -f 3 >'+Main_location_bho

###########################################################################################################################

##############################################################################################################################
#BHO_un
Main_location_bho_un='/tmp/Main_un.txt'
Sub_loction_BHO_un="\\bin\\Win32"
Output_location_un='/nas/QA/Robert/mediy/Output_u.txt'
Ootput_txt_BHO_un = 'test1.txt'
Output_location_W_un="\\\\nas\\public\\QA\\Robert\\mediy\\Output_u.txt"
#Comands
comand_i_un='cat /var/lib/jenkins/jobs/BHO_uninstaller_Builder/lastSuccessful/log|grep "Copy to"|cut -d " " -f 3 >'+Main_location_bho_un
###########################################################################################################################



