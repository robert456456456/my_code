import urllib2
import subprocess
import os
import time
import zlib
import sys
import shutil
import httplib
import random
import MySQLdb

array32=[]
array64=[]
hren = 0
x64=""
x86=""
week = 60*60*24*7
domainCount = 0
brandCount = 0
forbidden = [404,400,401,402,403,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,422,423,424,425,429,431,440,444,449,450,451,494,496,496,497,499,500,501,502,503,504,505,506,507,508,509,510,511,520,522,523,524,598,599]
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
	try:
		x64=""
		x86=""
		crc64=""
		crc32=""
		size=0
		test = get_status_code(host, "/"+param)
		print test
		if test not in forbidden:
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
			size = os.path.getsize(os.getcwd()+"\\"+"extensions"+"\\"+fname)
			subprocess.Popen([os.getcwd()+'\craparc.exe','-x',os.getcwd()+"\\"+"extensions"+"\\"+fname,os.getcwd()+"\\"+"extensions"+"\\"+a], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
			time.sleep(15)
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
			return [crc32,crc64,x86,x64,size,fname,test]
		else:
			return [test,"server return","","",0,"",test]
	except:
		return["failed","download","","",0,"",0]

def insertToDB(crc32, crc64, file_size,fname,status,domain,brand):

    conn = MySQLdb.connect(host= "dbase.webpick.net", user="admin", passwd="Go512625",db="zach_test")
    x = conn.cursor()
    query = "INSERT INTO ivgy_bot VALUES(now(),'"+str(crc64)+"','"+str(crc32)+"',"+str(file_size)+",'"+fname+"',"+str(status)+",'"+domain+"','"+brand+"')"
    print "Insert : "+query
    x.execute(query)
    conn.commit()

    conn.close()

def domainList(x):
    return {
        0: "installerdownloadmy.ru",
        1: "draivermagicfast.info",
        2: "solutioncustoml.info",
        3: "mastercanadain.info",
        4: "zillioncompletee.info",
        5: "superstoragemy.info",
        6: "documentsitefun.info",
        7: "applicationgrabb.info",
    }[x]

def brandList(x):
    return {
        0: "svr",
        1: "cousc",
        2: "sftc",
        3: "csaco",
        4: "disli",
        5: "sapr",
        6: "dfp",
        7: "fds",
		8: "smrtc",
		9: "atu",
		10: "wow",
		11: "fsr",
		12: "pro",
		13: "tpf",
		14: "ske",
		15: "dkpp",
		16: "skit",
		17: "great",
		18: "webs",
		19: "safer",
		20: "snet",
		21: "sbox",
		22: "saon",
		23: "prd",
		24: "d2d",
		25: "d4m",
		26: "d4r",
		27: "dep",
		28: "dsl",
		29: "e2s",
		30: "its",
		31: "l2p",
		32: "s2u",
		33: "svs",
		34: "snd",
		35: "tpb",
		36: "cpk",
		37: "tad",	
    }[x]
	
while True:
	
	randomNum = random.randrange(999999)
	randomMode = random.randrange(0,3,2)
	full= run_file(domainList(domainCount),'?e='+brandList(brandCount)+'&sfx=2&cht='+str(randomMode)+'&publisher=1&ind=1959754246391789454&exid=0&ssd=2796699686421963424&hid=17493129533580555503&osid=603&fc=1&randstring='+str(randomNum))
	insertToDB(full[0], full[1], full[4],full[5],full[6],domainList(domainCount),brandList(brandCount))
	time.sleep(60)
	domainCount = domainCount + 1
	brandCount = brandCount + 1
	if domainCount == 8:
		domainCount=0
	if brandCount == 38:
		brandCount = 1
	for path,dirs,files in os.walk(os.getcwd()+"\\"+"extensions"):
		for fn in files:
			dirpath = os.path.join(path,fn)
			if int(time.time() - os.path.getmtime(dirpath)) > week:
				try:
					os.remove (dirpath)
				except:
					pass
