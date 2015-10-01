import subprocess
import _winreg
import time
import os
import json
import sys
import time
import sqlite3
import shutil
import urllib2
import ConfigParser




def download(link):

    url = link
    u = urllib2.urlopen(url)
    meta = u.info()
    name = str(meta.getheaders("Content-Disposition"))
    fname = name[24:-3]
    if not os.path.exists(os.getcwd()+"\\"+"downloads"):
        os.makedirs(os.getcwd()+"\\"+"downloads")
    f = open(os.getcwd() + "\\" + "downloads" + "\\" + fname, 'wb')
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
    proc = subprocess.Popen(os.getcwd()+"\\"+"downloads\\"+fname, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    return fname

def unreg():
    _winreg.KEY_ALL_ACCESS
    array = []
    aReg = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
    aKey = _winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
    for i in range(1024):
        try:
            asubkey_name = _winreg.EnumKey(aKey,i)
            asubkey = _winreg.OpenKey(aKey,asubkey_name)
            val = _winreg.QueryValueEx(asubkey, "DisplayName")
            if val[0][0:3] != "CCC":
                array.append(val[0])
        except:
            pass
    return array


def procEx(name):
    loop = True
    while loop:
        loop = False
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if line[0:len(name)] == name or name in line:
                loop = True
        time.sleep(30)


def chromeEx():
	array = []
	try:
		if chexist:
			gExc = ["Store", "Gmail", "YouTube", "Chrome In-App Payments service", "Chrome", "Google Search", "Google Docs", "Google Drive", "Feedback", "Bookmark Manager", "Cloud Print", "Settings", "Google Wallet"]
			if winver in ["501", "502"]:
				googleFolder = os.environ['USERPROFILE'] +"\Local Settings\Application Data\Google\Chrome\User Data\Default"
			else:
				googleFolder = os.environ['USERPROFILE'] +"\AppData\Local\Google\Chrome\User Data\Default"
			jsonFile=open(googleFolder+"\Preferences", 'r').read()
			dump=json.loads(jsonFile)
			for x in dump['extensions']['settings']:
				if "manifest" in dump['extensions']['settings'][x]:
					if "name" in dump['extensions']['settings'][x]['manifest']:
						a = dump['extensions']['settings'][x]['manifest']['name']
						if not a in gExc :
							array.append(a)
				else:
					try:
						dev=dump['extensions']['settings'][x]['path']
						devFile=open(dev+"\manifest.json", 'r').read()
						devdump=json.loads(devFile)
						b = devdump['name']
						if b not in gExc:
							array.append(b)
					except:
						pass
		return array

	except:
		return ["Chrome extensions list not found"]


def firefoxEx():
	array = []
	try:
		if ffexist:
			if winver in ["501", "502"]:
				foxfolder = os.environ['USERPROFILE']+"\Application Data\Mozilla\Firefox\Profiles"
			else:
				foxfolder = os.environ['USERPROFILE']+"\AppData\Roaming\Mozilla\Firefox\Profiles"
			for dirname, dirnames, filenames in os.walk(foxfolder):
				# print path to all subdirectories first.
				for subdirname in dirnames:
					if ".default" in subdirname:
						#print subdirname
						extfolder = foxfolder+"\\"+subdirname
					#print subdirname
			#print extfolder
			shutil.copy(extfolder + r"\extensions.sqlite",os.getcwd()+r"\firefox.sqlite")
			time.sleep(60)
			data = sqlite3.connect("firefox.sqlite")
			cur = data.cursor()
			cur.execute('select a.id, b.name from addon as a, locale as b where b.id = a.defaultLocale')
			# extract column names
			column_names = [d[0] for d in cur.description]
			ffExt=""
			ffExc=['Default', 'FiddlerHook', 'Microsoft .NET Framework Assistant']
			for row in cur:
				# build dict
				info = dict(zip(column_names, row))
				# dump it to a json string
				reply = json.dumps(info)
				ffJson = json.loads(reply)
				if not ffJson['name'] in ffExc:
					array.append(ffJson['name'])
		return array
	except:
		return ['firefox extensions list not found']


def ieEx64():
	array = []
	try:
		if x64 == "1":
			_winreg.KEY_ALL_ACCESS
			aReg = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
			aKey = _winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects", 0, _winreg.KEY_READ | _winreg.KEY_WOW64_64KEY)
			for i in range(50):
				try:
					asubkey_name= _winreg.EnumKey(aKey, i)
					bKey = _winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects" + "\\" + asubkey_name, 0, _winreg.KEY_READ | _winreg.KEY_WOW64_64KEY)
					val = _winreg.QueryValueEx(bKey, "")
					if val[0] !="":
						array.append(val[0])
				except:
					pass
			return array
		else:
			return array
	except:
		return ["Internet Explorer 64 extensions list not found"]


def ieEx():
	array = []
	try:
		_winreg.KEY_ALL_ACCESS
		aReg = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
		aKey = _winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects", 0, _winreg.KEY_READ)
		for i in range(50):
			try:
				asubkey_name = _winreg.EnumKey(aKey,i)
				bKey = _winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects"+"\\" + asubkey_name, 0, _winreg.KEY_READ)
				val = _winreg.QueryValueEx(bKey, "")
				if val[0] != "":
					array.append(val[0])

			except:
				pass
		return array	
	except:
		return ["Internet Explorer extensions list not found"]
		

def difference(array1, array2):
	array=[]
	for x in array2:
		if x not in array1:
			array.append(x)
	return array
#end of functions
#main 
section = "config"
logPath = '\\\\192.168.1.210\\Public\\QA\\logs'
url = ""

config = ConfigParser.RawConfigParser()
config.read('cfg.ini')
url = str(config.get(section, 'url'))
logPath = str(config.get(section, 'logPath'))
cmd = 'WMIC PROCESS get Caption'

drive = os.environ['SYSTEMDRIVE']
ffexist = False
chexist = False
retries = 0

if os.path.isdir(drive + "\Program Files (x86)"):
        
	pf = drive + "\Program Files (x86)"
	x64 = "1"

else:
	pf = drive + "\Program Files"
	x64 = "0"


if os.path.isdir(drive + "\Program Files\Mozilla Firefox") or os.path.isdir(drive + "\Program Files (x86)\Mozilla Firefox"):
	ffexist = True

if os.path.isdir(drive + "\Program Files (x86)\Google\Chrome\Application") or os.path.isdir(drive + "\Program Files\Google\Chrome\Application"):
	chexist = True

	
if sys.getwindowsversion()[4] == "":
    sp = "Service Pack 0"
else:
    sp = str(sys.getwindowsversion()[4])

winver = str(sys.getwindowsversion()[0]) + "0" + str(sys.getwindowsversion()[1])
snapshot_1 = unreg()
ieext_1 = ieEx()
ieext64_1 = ieEx64()
ffext_1 = firefoxEx()
chext_1 = chromeEx()

while True:
    if retries == 4:
        try:
            log = open("log.txt", "wb")
            log.write("The server keeps returning 404 after 4 retries, fuck off!!!")
            log.close()
            shutil.copy2(r"log.txt", logPath + "\\" + winver + "_" + x64 + "_" + sp + " " + str(int(time.time())) + ".txt")
            sys.exit(0)
        except:
            log = open(logPath + "\\" + winver + "_" + x64 + "_" + sp + " " + str(int(time.time())) + ".txt", "wb")
            log.write("The server keeps returning 404 after 4 retries, fuck off!!!")
            log.close()
            sys.exit(0)
    try:
        process = download(url)
        break
    except:
        retries = retries + 1
time.sleep(60)
procEx(process)
time.sleep(60)

snapshot_2 = unreg()
ieext_2 = ieEx()
ieext64_2 = ieEx64()
ffext_2 = firefoxEx()
chext_2 = chromeEx()

snapshot_d = difference(snapshot_1, snapshot_2)
ieext_d = difference(ieext_1, ieext_2)
ieext64_d = difference(ieext64_1, ieext64_2)
ffext_d = difference(ffext_1, ffext_2)
chext_d = difference(chext_1, chext_2)


try:
    log = open("log.txt", "wb")
    log.write(winver + "_" + x64 + "_" + sp)
    log.write("\r\n")
    log.write("New programs: " + '\r\n   '.join(snapshot_d))
    log.write("\r\n")
    log.write("Firefox new extensions: " + '\r\n   '.join(ffext_d))
    log.write("\r\n")
    log.write("Chrome new extensions: " + '\r\n   '.join(chext_d))
    log.write("\r\n")
    log.write("Internet Explorer new extensions: " + '\r\n   '.join(ieext_d))
    log.write("\r\n")
    if x64 == "1":
        log.write("Internet Explorer 64 new extensions: " + '\r\n   '.join(ieext64_d))
    log.write("\r\n")
    log.write("Download retries count: " + str(retries))			
    log.close()

    shutil.copy2(r"log.txt", logPath + "\\" + winver + "_" + x64 + "_" + sp + " " + str(int(time.time())) + ".txt")

except:
    log = open(logPath + "\\" + winver + "_" + x64 + "_" + sp + " " + str(int(time.time())) + ".txt", "wb")
    log.write(winver + "_" + x64 + "_" + sp)
    log.write("\r\n")
    log.write("New programs: " + '\r\n   '.join(snapshot_d))
    log.write("\r\n")
    log.write("Firefox new extensions: " + '\r\n   '.join(ffext_d))
    log.write("\r\n")
    log.write("Chrome new extensions: " + '\r\n   '.join(chext_d))
    log.write("\r\n")
    log.write("Internet Explorer new extensions: " + '\r\n   '.join(ieext_d))
    log.write("\r\n")
    if x64 == "1":
        log.write("Internet Explorer 64 new extensions: " + '\r\n   '.join(ieext64_d))
    log.write("\r\n")
    log.write("Download retries count: " + str(retries))
    log.close()

#end main