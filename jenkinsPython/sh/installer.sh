#!/bin/bash
args=
for arg in "$@";
do
  args="$args '$arg'"
done
export MY_VAR=$arg
#eval exec my_command $args
echo   $args
#echo $tape
# premition to folder i need work 
chmod 755 /nas/QA/Andrey/report/ROBOT/ButtonExtensions/*
chmod 755 /nas/QA/Andrey/report/ROBOT/Vaudix/*
chmod 755 /nas/QA/Andrey/report/ROBOT/Gadget/*
chmod 755 /nas/QA/Andrey/report/ROBOT/FileSave/*
chmod 755 /nas/QA/Andrey/report/ROBOT/New_Installer/*
chmod 755  /nas/QA/Andrey/report/ROBOT/Ongoing/*
#clean foders and content inside
rm /nas/QA/Andrey/report/ROBOT/Success/*
rm -rf  /nas/QA/Andrey/report/ROBOT/ButtonExtensions/*
rm -rf /nas/QA/Andrey/report/ROBOT/Vaudix/*
rm -rf  /nas/QA/Andrey/report/ROBOT/Gadget/*
rm -rf  /nas/QA/Andrey/report/ROBOT/FileSave/*
rm -rf  /nas/QA/Andrey/report/ROBOT/New_Installer/*
rm -rf  /nas/QA/Andrey/report/ROBOT/Ongoing/*
#atach file for send mail
pwd
touch /nas/QA/Andrey/report/ROBOT/Success/mails
#loop parmetar i
i=0
# power on vm for test in python
python /nas/QA/Robert/html/python/remotevmLPOA.py  $MY_VAR
# loop wait when test end checking count of txt files  inside folder if they exsit loop stops  
for i in {1..480}
do
#rm -rf  /nas/QA/Andrey/report/ROBOT/FileSave/*
#watcher on folder every 10 second and check if text file exist and check if vm power off 
c=$(ls -l /nas/QA/Andrey/report/ROBOT/Success/*.txt | wc -l)
if [ $c -eq 8 ]
then
echo test end
else
#rm -rf  /nas/QA/Andrey/report/ROBOT/FileSave/*
#if vm power off with python script do revettocarent snapshot and power on vm test can be continued
echo test run and power on vm
python /nas/QA/Robert/html/python/remotevm.py  $MY_VAR
sleep 10
fi
done
#then loop end i check again count of txt files  inside folder and send mail if fail or success
c1=$(ls -l /nas/QA/Andrey/report/ROBOT/Success/*.txt | wc -l)
if [ $c1 -eq 8 ]
then
#check count of txt files  inside folder and send mail
echo $count files found > mails
#ls -l /nas/QA/Andrey/report/ROBOT/Success/*.txt >> /nas/QA/Andrey/report/ROBOT/Success/mails
mail -s "Installer_propect" robert@web-pick.com < /nas/QA/Andrey/report/ROBOT/Success/mails
else
echo not enough files found > mails
#ls -l /nas/QA/Andrey/report/ROBOT/Success/*.txt >> /nas/QA/Andrey/report/ROBOT/Success/mails 
mail -s "Installer_propect-test-end" robert@web-pick.com < /nas/QA/Andrey/report/ROBOT/Success/mails
fi
python /nas/QA/Robert/html/python/remotevmLPOpw.py  $MY_VAR


exit 0
