#!/bin/sh
#part 1 shh-54.200.2.201
chmod 777 /usr/share/nginx/extensions_dc/scrambler/qa_dir/
pushd /usr/share/nginx/extensions_dc/files/scrambled/qa/1/
srcdir="/usr/share/nginx/extensions_dc/files/scrambled/qa/1/crx"
dstdir="/usr/share/nginx/extensions_dc/scrambler/qa_dir/"
srcfile="/usr/share/nginx/extensions_dc/files/scrambled/qa/1/crx/___[##bg_script_name##].js"
cp $srcfile $dstdir/$dstfile
f1="/usr/share/nginx/extensions_dc/scrambler/qa_dir/___[##bg_script_name##].js "
f2="/usr/share/nginx/extensions_dc/scrambler/qa_dir/old.js "
mv -u $f1 $f2
popd
#part2 shh-54.200.2.201
chmod 777 /usr/share/nginx/extensions_dc/scrambler/qa_dir/
pushd /usr/share/nginx/extensions_dc/files/scrambled/qa/1/
srcdir="/usr/share/nginx/extensions_dc/files/scrambled/qa/1/xpi/content"
dstdir="/usr/share/nginx/extensions_dc/scrambler/qa_dir/"
srcfile="/usr/share/nginx/extensions_dc/files/scrambled/qa/1/xpi/content/___bg.js"
cp $srcfile $dstdir/$dstfile
f1="/usr/share/nginx/extensions_dc/scrambler/qa_dir/___bg.js "
f2="/usr/share/nginx/extensions_dc/scrambler/qa_dir/old1.js "
mv -u $f1 $f2
popd


#part3 shh-192.168.1.245
rm /nas/QA/Robert/html/python/paramTest/*
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
#part 4 shh-54.200.2.201
pushd /usr/share/nginx/extensions_dc/scrambler/qa_dir
chmod 777  /usr/share/nginx/extensions_dc/scrambler/qa_dir/old.js
chmod 777 /usr/share/nginx/extensions_dc/files/scrambled/qa/1/crx/___[##bg_script_name##].js
file1= '/usr/share/nginx/extensions_dc/files/scrambled/qa/1/crx/___[##bg_script_name##].js'
file2= '/usr/share/nginx/extensions_dc/scrambler/qa_dir/old.js'
cmp --silent $file1 $file2 || echo "files are different"
popd
#part 5 shh-54.200.2.201
pushd /usr/share/nginx/extensions_dc/scrambler/qa_dir
chmod 777  /usr/share/nginx/extensions_dc/scrambler/qa_dir/old1.js
chmod 777 /usr/share/nginx/extensions_dc/files/scrambled/qa/1/xpi/content/___bg.js
file1= '/usr/share/nginx/extensions_dc/files/scrambled/qa/1/xpi/content/___bg.js'
file2= '/usr/share/nginx/extensions_dc/scrambler/qa_dir/old1.js'
cmp --silent $file1 $file2 || echo "files are different"
popd
#part 6 shh-192.168.1.245
curl http://192.168.1.245/exst.php?sr=7
#part 7 run regretion exstention
#part 8 shh-192.168.1.245
pushd /nas/QA/Robert/html/python
file=$(cat /var/lib/jenkins/jobs/exstention\ regretion/lastStable/log)
echo $file > bob10.txt
File1=/nas/QA/Robert/html/python/bob10.txt
grep -q "Netscape 5-succses" /nas/QA/Robert/html/python/bob10.txt && exit 0 || exit 1
grep -q "Microsoft Internet Explorer 9.0-succses" /nas/QA/Robert/html/python/bob10.txt && exit 0 || exit 1
grep -q "Chrome 31.0.1650.63-succses" /nas/QA/Robert/html/python/bob10.txt && exit 0 || exit 1
grep -q "Firefox 26.0-succses" /nas/QA/Robert/html/python/bob10.txt && exit 0 || exit 1
popd


#part 8 shh-192.168.1.245
rm /nas/QA/Robert/html/python/paramTest/*
pushd /nas/QA/Robert/html/python/paramTest/
wget http://extensions_dc.webpick.net/scrambler/prod.php
test=$(cat prod.php | grep OK)
if (test==OK)
then
	rm /nas/QA/Robert/html/python/paramTest/prod.php
else
	exit 1
fi
popd
#part 9 shh-192.168.1.245
curl http://192.168.1.245/exst.php?sr=8
#part 10 run regretion exstention


#part 11 shh-192.168.1.245
pushd /nas/QA/Robert/html/python
file=$(cat /var/lib/jenkins/jobs/exstention\ regretion1/lastStable/log)
echo $file > bob10.txt
File1=/nas/QA/Robert/html/python/bob10.txt
grep -q "Netscape 5-succses" /nas/QA/Robert/html/python/bob10.txt && echo ok ||  echo faild
grep -q "Microsoft Internet Explorer 9.0-succses" /nas/QA/Robert/html/python/bob10.txt && echo ok ||  echo faild
grep -q "Chrome 31.0.1650.63-succses" /nas/QA/Robert/html/python/bob10.txt && echo ok ||  echo faild
grep -q "Firefox 26.0-succses" /nas/QA/Robert/html/python/bob10.txt && exit 0 || exit 1
popd

pwd
touch /nas/QA/Robert/html/python/paramTest/mail
echo Failed > /nas/QA/Robert/html/python/paramTest/mail
mail -s "JS recompilation" robert@web-pick.com < /nas/QA/Robert/html/python/paramTest/mail
mail -s "JS recompilation" noam@web-pick.com < /nas/QA/Robert/html/python/paramTest/mail
mail -s "JS recompilation" itai@web-pick.com < /nas/QA/Robert/html/python/paramTest/mail
mail -s "JS recompilation" zach@web-pick.com < /nas/QA/Robert/html/python/paramTest/mail


