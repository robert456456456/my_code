#!/bin/sh
pushd /nas/QA/Robert/html/python/
mkdir -p /nas/QA/Robert/html/python/bob/
srcdir="/nas/QA/Robert/html/python/bob1"
dstdir="/nas/QA/Robert/html/python/bob"
srcfile="/nas/QA/Robert/html/python/bob1/bob.txt"
cp $srcfile $dstdir/$dstfile
mv -u /nas/QA/Robert/html/python/bob/bob.txt /nas/QA/Robert/html/python/bob/backup.txt
file1=`/nas/QA/Robert/html/python/bob1/bob.txt`
file2=`/nas/QA/Robert/html/python/bob/backup.txt`
if [ "$file1" == "$file2" ]
then
    echo "Files have the same content"
else
    echo "Files have NOT the same content"
fi
popd

cat /var/lib/jenkins/jobs/exstention\ regretion/lastStable/log




chmod 755  /nas/QA/Robert/html/python/bob1/*
chmod 755 /nas/QA/Robert/html/python/bob/*

source_file=`/nas/QA/Robert/html/python/bob1/bob.txt`
dest_file=`/nas/QA/Robert/html/python/bob/backup.txt`
if cmp -s "$source_file" "$dest_file"; then
    echo files are the same
else
     echo files are different
fi




if egrep -wl 'Microsoft Internet Explorer 9.0-succses' "$filename" 1>/dev/null; then
  if egrep -wl 'Netscape 5-succses ' "$filename" 1>/dev/null; then
    if egrep -wl 'Firefox 26.0-succses' "$filename" 1>/dev/null; then
       if egrep -wl 'Chrome 31.0.1650.63-succses ' "$filename" 1>/dev/null; then
      echo "found all three words"
     fi
    fi
  fi