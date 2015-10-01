#!/bin/bash
args=
for arg in "$@";
do
  args="$args '$arg'"
done
export MY_VAR=$arg
echo $MY_VAR
Task=""
shark =""
echo -n $Task >   /nas/QA/Robert/html/test/exstcontear.txt
echo -n $shark  >  /nas/QA/Robert/html/test/bshitcock1.txt
chmod 755 /nas/QA/Robert/Robert/rlog/*
chmod 755 /nas/QA/Robert/html/test/logs/*
rm -rf /nas/QA/Robert/Robert/rlog/*
rm -rf /nas/QA/Robert/html/test/logs/*
python /nas/QA/Robert/html/python/remotevmLPOA.py $MY_VAR
for i in {1..400}
 do
  c=$(ls -l /nas/QA/Robert/Robert/rlog/*.txt | wc -l)
 if [ $c -eq 7 ]
then
echo test end
else
echo test run
sleep 10
fi
done
FILES=/nas/QA/Robert/html/test/logs/*
for f in $FILES
do
value=$(<$f)
done
echo "$value"
cat $FILES
exit 0
