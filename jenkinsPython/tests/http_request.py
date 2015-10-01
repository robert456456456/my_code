'''
Created on Oct 21, 2013

@author: Robert Adin
'''
#!/usr/bin/python
import random

import urllib2
import os
import time
import httplib

'''
from Tools.Scripts.patchcheck import status

URL1 = os.getenv('http://sweetjet.net')
URL2 = os.getenv('/?e=svon&cht=2&dcu=1&cpatch=2&dcs=1&pf=1&clsb=1&rbrt_log=c:\\temp\log.txt&publisher=9495&country=IL&ind=7812909272256438105&exid=0&ssd=7237547942674221734&hid=15156100130548037117&osid=601&channel=0&sfx=1&jc=1&category_name=SaveOnLH&install_date=20130602')
URL3 = URL1
req = urllib2.urlopen(URL1)
print req
'function for request with delay'
loopCounter = 1000
delay = 5
def nudnik(URL3):
    a = 1
    while a <= loopCounter:

        u = urllib2.urlopen(URL3)
        print u.info()
        time.sleep(delay)
        a = a + 1

#nudnik('http://getmeegan.info')
'''''


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


def run_file(host, param, name1):
    test = get_status_code(host, "/" + param)
    print test
    if test != 404:
        if not os.path.exists(os.getcwd() + "\\" + "extensions"):
            #print 1
            os.makedirs(os.getcwd() + "\\" + "extensions")
        url = 'http://' + host + "/" + param
        u = urllib2.urlopen(url)
        meta = u.info()
        name = str(meta.getheaders("Content-Disposition"))
        fname = name1
        f = open(os.getcwd() + "\\" + "extensions" + "\\" + fname, 'wb')
        a = fname[0:len(fname) - 4]
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
            status = status + chr(8) * (len(status) + 1)
            print status,
        f.close()
    return status


def multiplyD(loopCounter, delay, url,name):
    randomshit = random.randrange(99999999)
    a = 1
    param1 = '?e=smrtc&sfx=1&publisher=1&ind=1959754246391789454&exid=0&ssd=2796699686421963424&hid=17493129533580555503&osid=603'

    #while a <= loopCounter:

    run_file(url, param1,name)
    #time.sleep(delay)
    # a = a + 1


multiplyD(1, 1, 'ec2-54-200-7-6.us-west-2.compute.amazonaws.com','bp.exe')
''''
hren=1
while hren<10:
    #multiplyD(10,1,'ec2-54-187-243-98.us-west-2.compute.amazonaws.com')

    #multiplyD(10,1,'ec2-54-200-7-4.us-west-2.compute.amazonaws.com')
    #multiplyD(10,1,'ec2-54-191-233-163.us-west-2.compute.amazonaws.com')
    #multiplyD(10,1,'ec2-54-200-6-255.us-west-2.compute.amazonaws.com')
    #multiplyD(10,1,'ec2-54-200-6-236.us-west-2.compute.amazonaws.com')
    hren=hren+1
    '''
