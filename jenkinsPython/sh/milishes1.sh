#!/bin/bash
pwd
rm /nas/QA/Andrey/report/ROBOT/LP/Success/*
touch /nas/QA/Andrey/report/ROBOT/LP/mail
 i=0
 for i in {1..5}
 do
 c=$(ls -l /nas/QA/Andrey/report/ROBOT/LP/Success/*.txt | wc -l)

 if [ $c -eq 4 ]
 then
 echo 4 files found >  /nas/QA/Andrey/report/ROBOT/LP/mail

 ls -l /nas/QA/Andrey/report/ROBOT/LP/Success/*.txt>> mail
newfold1=$(date | awk '{print $3 $2 $6}')



mail -s "test" robert@web-pick.com < /nas/QA/Andrey/report/ROBOT/LP/mail
#echo "attached MaliciousIE10" | mail e "mailfrom Jnkins"robert@web-pick.com
#echo "attached MaliciousIE9" | mail -a /nas/QA/Andrey/report/ROBOT/LP/MaliciousIE9.txt -s "mailfrom Jnkins"robert@web-pick.com
#echo "attached MaliciousIE8" | mail -a /nas/QA/Andrey/report/ROBOT/LP/MaliciousIE8.txt -s "mailfrom Jnkins"robert@web-pick.com
#echo "attached MaliciousIE11" | mail -a /nas/QA/Andrey/report/ROBOT/LP/MaliciousIE11.txt -s "mailfrom Jnkins"robert@web-pick.com


#this is example to how to send mail with attachment 
#echo "attached MaliciousIE10" | mail -a /nas/QA/Andrey/report/ROBOT/LP/MaliciousChro.txt -s "mailfromBot" vartoso.blusnap@gmail.com

echo "newfold1:" $newfold1

mkdir -p  /nas/QA/Andrey/reports/${BUILD_NUMBER}/$newfold1/

cp /nas/QA/Andrey/report/ROBOT/LP/* /nas/QA/Andrey/reports/${BUILD_NUMBER}/$newfold1/

rm /nas/QA/Andrey/report/ROBOT/LP/Success/*
 else
IE8="Milishes_IE8"
IE9="Milishes_IE9"
IE10="Milishes_IE10"
IE11="Milishes_IE11"
p1="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE11.txt"
p2="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE9.txt"
p3="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE10.txt"
p4="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE8.txt"
#pushd /nas/QA/Robert/html/python
#chmod 755 /nas/QA/Robert/html/python/test.sh
#dos2unix  /nas/QA/Robert/html/python/test.sh
#./test.sh
#popd

if [ $i -eq 2 ]; then
   echo In process IE9
	python /nas/QA/Robert/html/python/remotevmPw.py section=$IE11
	cat > $p1
	sleep 50
	python /nas/QA/Robert/html/python/remotevm.py section=$IE9
elif [ $i-eq 3 ]; then
echo In process IE10
	python /nas/QA/Robert/html/python/remotevmPw.py section=$IE9
	cat > $p2
	sleep 50
	python /nas/QA/Robert/html/python/remotevm.py section=$IE10
elif [ $i-eq 4  ]; then
echo In process IE8	
python /nas/QA/Robert/html/python/remotevmPw.py section=$IE10
	cat > $p3
	sleep 50
python /nas/QA/Robert/html/python/remotevm.py section=$IE8
elif [ $i-eq 5  ]; then
python /nas/QA/Robert/html/python/remotevmPw.py section=$IE8
	cat > $p4
	sleep 50
	else
	echo In process IE11
python /nas/QA/Robert/html/python/remotevm.py section=$IE11
fi
sleep 7200
fi 
done

echo not enough files found > /nas/QA/Andrey/report/ROBOT/LP/mail
ls -l /nas/QA/Andrey/report/ROBOT/LP/*.txt >>mail
mail -s "faild" robert@web-pick.com </nas/QA/Andrey/report/ROBOT/LP/mail



echo "newfold2:" $newfold2

mkdir -p /nas/QA/Andrey/reports/${BUILD_NUMBER}/$newfold2/
ls -la /nas/QA/Andrey/reports
ls -la /nas/QA/Andrey/reports/${BUILD_NUMBER}
ls -la /nas/QA/Andrey/reports/${BUILD_NUMBER}/$newfold2/

cp /nas/QA/Andrey/report/ROBOT/LP/* /nas/QA/Andrey/reports/${BUILD_NUMBER}/$newfold2/
exit 0