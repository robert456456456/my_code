from jenkinsPython.run_local_vm.tipot import function_class

__author__ = 'Robert Adinihu'
array1 = ['/nas2/AV_logs/7 Ultimate x64 sp1 Office4 EmsiSoft1.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 F-Secure.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Symantec (Norton).txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Rising.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 CAT-QuickHeal.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 nProtect.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 ESET-NOD32.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 TrendMicro.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Ikarus.txt', '/nas2/AV_logs/7_Ultimate_x64_sp1_Office4_BitDefender.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Microsoft SE.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Agnitum.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 GData.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 NANO-Antivirus.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Avast.txt', '/nas2/AV_logs/mail', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 VIPRE.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Sophos.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Fortinet.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 ViRobot.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Malwarebytes.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 AntiVir (Avira).txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 K7AntiVirus.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 ClamAV (Immunet).txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 McAfee.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Antiy-AVL.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Panda.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Ahn-Lab-V3.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 TotalDefense (CA).txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 AVG.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Norman.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 F-Prot.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 PCTools.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 DrWeb.txt', '/nas2/AV_logs/7_Ultimate_x64_sp1_Office4_Kaspersky.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 SUPERAntiSpyware.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Kingsoft.txt', '/nas2/AV_logs/7 Ultimate x64 sp1 Office4 Comodo.txt']
path="/nas2/AV_logs"
print path
bob= function_class.function()
array2=bob.folder(path)
ar3= bob.difference(array2,array1)
print ar3


