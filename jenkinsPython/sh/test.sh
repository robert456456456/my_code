#!/bin/bash
IE8="Milishes_IE8"
IE9="Milishes_IE9"
IE10="Milishes_IE10"
IE11="Milishes_IE11"
p1="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE11.txt"
p2="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE9.txt"
p3="/nas/QA/Andrey/report/ROBOT/LP/Success/SuccessIE10.txt"
p4="/nas/QA/Andrey/report/ROBOT/LP/Success/"
if [[ -f $p2 && -f $p1]];then

    echo In process IE10
python /nas/QA/Robert/html/python/remotevmA.py section=$IE10
sleep 600
rm $p2	
elif [[ -f $p3 ]]; then
    echo In process IE8
	python /nas/QA/Robert/html/python/remotevmA.py section=$IE8
cat > $p2
cat > $p1
elif [[ -f $p1 ]];then
    echo In process IE9
	
python /nas/QA/Robert/html/python/remotevmA.py section=$IE9
sleep 600	
else
echo In process IE11
python /nas/QA/Robert/html/python/remotevmA.py section=$IE11 
  fi
 exit 0