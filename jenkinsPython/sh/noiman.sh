IE8="Noyman_2"
IE9="Noyman_3"
IE10="Noyman_4"
if [[ -f l /nas/QA/Andrey/report/ROBOT/Noyman/ReportSuccessIE11.txt ]] ; then
    echo file exists.
python /nas/QA/Robert/html/python/remotevm.py section=$IE9
fi
if [[ -f l /nas/QA/Andrey/report/ROBOT/Noyman/Report/SuccessIE9.txt ]] ; then
    echo file exists.
python /nas/QA/Robert/html/python/remotevm.py section=$IE10
fi
if [[ -f l /nas/QA/Andrey/report/ROBOT/Noyman/Report/SuccessIE10.txt ]] ; then
    echo file exists.
python /nas/QA/Robert/html/python/remotevm.py section=$IE8
fi