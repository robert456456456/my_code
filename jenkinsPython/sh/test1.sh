#!/bin/sh
pushd /nas/QA/Robert/html/python/paramTest/
wget http://extensions_dc.webpick.net/scrambler/scramble.php
test=$(cat  scramble.php | grep OK)
if (test==OK)
then
rm /nas/QA/Robert/html/python/paramTest/scramble.php
else
exit 1
fi
popd
pushd /nas/QA/Robert/html/python/paramTest/
s="DONE"
wget http://extensions_dc.webpick.net/scrambler/check.php
test=$(cat check.php | grep $s)
chmod 777 check.php
if (test==DONE)
then
curl http://192.168.1.245/exst.php?sr=7
rm /nas/QA/Robert/html/python/paramTest/check.php
else
exit 1
fi
popd





