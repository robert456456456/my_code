import httplib
import urllib2
import subprocess
import os
import time
import zlib
import sys
import shutil
import random

array32=[]
array64=[]
hren = 0
x64=""
x86=""

def crc(fileName):
    prev = 0
    for eachLine in open(fileName,"rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)

def get_status_code(host, path="/"):
    """ This function retreives the status code of a website by requesting
        HEAD data from the host. This means that it only requests the headers.
        If the host cannot be reached or something else goes wrong, it returns
        None instead.
    """
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None

def run_file(host, param):
	test = get_status_code(host, "/"+param)
	print test
	if test != 404:
		if not os.path.exists(os.getcwd()+"\\"+"extensions"):
			#print 1
			os.makedirs(os.getcwd()+"\\"+"extensions")
		url = 'http://'+host+"/"+param
		u = urllib2.urlopen(url)
		meta = u.info()
		name = str(meta.getheaders("Content-Disposition"))
		fname = name[24:-3]
		f = open(os.getcwd()+"\\"+"extensions"+"\\"+fname, 'wb')
		a = fname[0:len(fname)-4]
		file_size = int(meta.getheaders("Content-Length")[0])
		print "Downloading: %s Bytes: %s" % (fname, file_size)
		file_size_dl = 0
		block_sz = 8192
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break
		
			file_size_dl += len(buffer)
			f.write(buffer)
			status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
			status = status + chr(8)*(len(status)+1)
			print status,
		f.close()
	subprocess.Popen([os.getcwd()+'\craparc.exe','-x',os.getcwd()+"\\"+"extensions"+"\\"+fname,os.getcwd()+"\\"+"extensions"+"\\"+a], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
	time.sleep(10)
	#print os.getcwd()+'\craparc.exe '+'-x '+ os.getcwd()+"\\"+fname,os.getcwd()+"\\"+a
	path = r'C:\abc\def\ghi'  # remove the trailing '\'
	for root, dirs, files in os.walk(os.getcwd()+"\\"+"extensions"+"\\"+a):
		for file in files:
			if file.endswith(".x64.dll"):
				x64 = os.path.join(root, file)
			elif file.endswith(".dll"):
				x86 = os.path.join(root, file)
			elif file.endswith(".exe"):
				binary = file
	#print "x64: "+x64
	#print "x86: "+x86
	crc64 = crc(x64)
	crc32 = crc(x86)
	#print crc64
	#print crc32
	config = open(os.getcwd()+'\config.txt',"wb")
	config.write(';!@Install@!UTF-8!')
	config.write('\r\n')
	config.write('Progress="No"')
	config.write('\r\n')
	config.write('ExecuteFile="'+binary+'"')
	config.write('\r\n')
	config.write(';!@InstallEnd@!')
	config.close()
	
	bat = open('sfx-creator.bat',"wb")
	bat.write('@setlocal enableextensions')
	bat.write('\r\n')
	bat.write('@cd /d "%~dp0"')
	bat.write('\r\n')
	bat.write('set p=%~dp0')
	bat.write('\r\n')
	bat.write('set _7zip="c:\Program Files\\7-Zip\\7z.exe"')
	bat.write('\r\n')
	bat.write('pushd '+os.getcwd()+"\\"+"extensions"+"\\"+a)
	bat.write('\r\n')
	bat.write('%_7zip% a -r %p%\exstention.7z .')
	bat.write('\r\n')
	bat.write('popd')
	bat.write('\r\n')
	bat.write('copy /b 7zS.sfx + config.txt + exstention.7z '+str(hren)+".exe")
	bat.write('\r\n')
	bat.write('%_7zip% l '+str(hren)+".exe")
	bat.close()
	proc = subprocess.Popen(os.getcwd()+"\sfx-creator.bat", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
	time.sleep(10)
	#shutil.copy2(str(hren)+".exe","\\\\192.168.1.210\Public\QA\Robert\html\compiler_exe\\"+str(hren)+".exe")
	os.remove(os.getcwd()+"\\"+"sfx-creator.bat")
	os.remove(os.getcwd()+"\\"+"exstention.7z")
	os.remove(os.getcwd()+"\\"+"config.txt")
	#os.remove(os.getcwd()+"\\"+str(hren)+".exe")
	
	return [crc32,crc64,x86,x64]



while hren<100:
	randomshit=random.randrange(99999999)
	full= run_file("solutioncustoml.info",'?e=smrtc&sfx=1&cht=0&publisher=1&ind=1959754246391789454&exid=0&ssd=2796699686421963424&hid=17493129533580555503&osid=603&fc=1&randomshit='+str(randomshit))
	#print os.getcwd()
	if full[0] in array32:
		print "file didn't change: "+full[2] +" count: "+str(hren)
		break
	if full[1] in array64:
		print "file didn't change: "+full[3] +" count: "+str(hren)
		break
	array32.append(full[0])
	array64.append (full[1])
	time.sleep(60)
	hren = hren+1



print array32
print array64
