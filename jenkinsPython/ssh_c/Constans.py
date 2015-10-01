__author__ = 'Robert adinhy'

QA_Builder_url = "qa.ext.build.web-pick.com"
#extention bulder domains
Brand_Main = "Main"
Brand_Fallback_1 = "Fallback 1"
Brand_Fallback_2 = "Fallback 2"
Brand_Primary_Update = "Primary Update"
Brand_Panda_1 = "Panda 1"
Brand_Panda_2 = "Panda 2"
Brand_Media_Buying = "Media Buying "
Brand_Teddy = "Teddy"
Brand_Zet = "Zet"
brand_c_bi = 'bijo'
brand_c_bh = 'BHO'
brand_c_un = 'Unin'
brand_c_ff = 'FF_S'
brand_c_al = 'All'
brand_c_i = 'installer'

Main_Builder_url = "54.149.75.132"
Fallback_1_Builder_url = "54.69.219.247"
Fallback_2_Builder_url = "54.68.254.5"
Primary_Update_Builder_url = "54.68.32.164"
Panda_1_Builder_url = "54.148.138.117"
Panda_2_Builder_url = "54.68.117.129"
Media_Buying_Builder_url = "54.69.18.207"
Teddy_Builder_url = "54.187.148.13"
Zet_Builder_url = "54.200.238.109"
#instuller domains
Type_FS_Servers1=""
Type_FS_Servers11=""
Type_FS_Servers2 = ""
Type_FS_Servers3="54.149.241.47"
Type_FS_Servers4="54.69.228.231"
Type_lpo_Servers="54.68.13.248"
Type_lpo_Servers1="54.213.72.9"
Type_lpo_Servers2="54.200.195.191"
Type_lpo_Servers3="52.10.14.196"
Type_lpo_Servers4=""
Type_lpo_Servers5=""
Type_MB_Servers="54.149.14.235"
Type_lpo_Servers6="54.191.16.149"

I_type="FS"
I_type1="lpo"
I_type2="MB"

port= 27628
user="root"
pw_i="Yd512625!!"
pw= 'Wp512625!!'


#installer check modifi date
comand_i="sh /home/replicator/replication.sh"
comand_i1="ls -la /usr/share/nginx/html/compilation/installer/websites/installer/installmate/scripts/versions/1; date"
comand_i11="ls -la /usr/share/nginx/html/compilation/installer/websites/installer/installmate/pic_installer/versions/1; date"
#All Extention components
comand_all_r="rm -rf /usr/share/compiler"
comand_all_c="rsync -vaz --whole-file -q --delete -r -e 'ssh -p 27628' root@54.69.155.182:/usr/share/compiler/* /usr/share/compiler/"
comand_all_m="ls -la /usr/share/compiler; dete"
#firefox silicon
comand_f_r = "rm -rf /usr/share/compiler/FF_S"
comand_f_c="rsync -vaz --whole-file -q --delete -r -e 'ssh -p 27628' root@54.69.155.182:/usr/share/compiler/FF_S/* /usr/share/compiler/FF_S"
comand_f_m="ls -la /usr/share/compiler; dete"

#bijo componets
comand_bi_r="rm -rf /usr/share/compiler/bijo"
comand_bi_c="rsync -vaz --whole-file -q --delete -r -e 'ssh -p 27628' root@54.69.155.182:/usr/share/compiler/bijo/* /usr/share/compiler/bijo"
#Bho components
comand_bh_r="rm -rf /usr/share/compiler/x32"
comand_bh_c="rsync -vaz --whole-file -q --delete -r -e 'ssh -p 27628' root@54.69.155.182:/usr/share/compiler/x32/* /usr/share/compiler/x32"
comand_bh_r1="rm -rf /usr/share/compiler/x64"
comand_bh_c1="rsync -vaz --whole-file -q --delete -r -e 'ssh -p 27628' root@54.69.155.182:/usr/share/compiler/x64/* /usr/share/compiler/x64"
comand_bh_r2="rm -rf /usr/share/compiler/tlb"
comand_bh_c2="rsync -vaz --whole-file -q --delete -r -e 'ssh -p 27628' root@54.69.155.182:/usr/share/compiler/tlb/* /usr/share/compiler/tlb/"
#BHO_Uninstuller
comand_bhu_r="rm -rf /usr/share/compiler/uninstaller"
comand_bhu_c="rsync -vaz --whole-file -q --delete -r -e 'ssh -p 27628' root@54.69.155.182:/usr/share/compiler/uninstaller/* /usr/share/compiler/uninstaller"


#rsync -vaz --whole-file -q --delete -r -e 'ssh -p 27628' root@54.69.155.182:/usr/share/compiler/FF_S/* /usr/share/compiler/FF_S

