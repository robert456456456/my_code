__author__ = 'Robert Adinihy'

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

cmd = 'WMIC PROCESS get Caption'


class function:
    def download(self, host, param):

        url = 'http://'+host+"/"+param
        u = urllib2.urlopen(url)
        meta = u.info()
        name = str(meta.getheaders("Content-Disposition"))
        fname = name[24:-3]
        if not os.path.exists(os.getcwd() + "\\" + "downloads"):
            os.makedirs(os.getcwd() + "\\" + "downloads")
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
            status = status + chr(8) * (len(status) + 1)
            print status,

        f.close()
        '''
        #proc = subprocess.Popen(os.getcwd() + "\\" + "downloads\\" + fname, shell=True, stdin=None, stdout=None,
                                stderr=None, close_fds=True)
        '''
        return fname

    def unreg(self, regpath):
        _winreg.KEY_ALL_ACCESS
        array = []
        # exsemle
        # regpath=r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        aReg = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
        aKey = _winreg.OpenKey(aReg, regpath)
        for i in range(1024):
            try:
                asubkey_name = _winreg.EnumKey(aKey, i)
                asubkey = _winreg.OpenKey(aKey, asubkey_name)
                val = _winreg.QueryValueEx(asubkey, "DisplayName")
                if val[0][0:3] != "CCC":
                    array.append(val[0])
            except:
                pass
        return array


    def procEx(self, name):
        """

        :param name:
        """
        loop = True
        while loop:
            loop = False
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            for line in proc.stdout:
                if line[0:len(name)] == name or name in line:
                    loop = True
            time.sleep(30)


    def difference(self, array1, array2):
        """

        :param array1:
        :param array2:
        :return:
        """
        array = []
        for x in array2:
            if x not in array1:
                array.append(x)
        # print array
        return array

    def folder(self, path1):
        array = []
        for path, dirs, files in os.walk(path1):
            for fn in files:
                array.append(os.path.join(path, fn))
                # print array
        return array

    def get_immediate_subdirectories(self, dir):
        return [name for name in os.listdir(dir)
                if os.path.isdir(os.path.join(dir, name))]

    def get_date(self, sub_paths, filename, start_index,main_path):
        for x in range(len(sub_paths)):
            a = x + start_index
            try:
                path = main_path + "\\" + sub_paths[a] + "\\" + filename
                seconds = os.path.getmtime(path)
                print time.strftime('%Y-%m-%d %H:%M', time.localtime(seconds))
                D_T = time.strftime('%Y-%m-%d %H:%M', time.localtime(seconds))
            except:
                break
            return (D_T)
    def run_local_vm(self, path_status_sh,path_status_txt,snap_sh):
        print(os.system(path_status_sh))
        f = open(path_status_txt, 'r')
        print f.read()
        bob = f.read()
        for x in range(0, 450):
            if bob in 'Total running VMs: 0':
                try:
                    #os.system('D:\\qa-automation\\jenkinsPython\\run_local_vm\\revert_snap_powerOn.sh')
                    os.system(snap_sh)
                    time.sleep(120)
                    os.system(path_status_sh)
                    bob = f.read()
                except:
                    print "end test "

    def copy(self, source, dest):


        shutil.copy2(source,dest)


        return



    def move_file_ctent_to_arry(self, file_path):
        arr = open(file_path, "r").readlines()
        temp = []
        for x in arr:
            x = x.replace("\n", "")
            temp.append(x)
        arr = temp
        return arr



    def find_file_with_exetentio(self,path,extention ):

        file_stuck=[]
        directory=path
        fileiter = (os.path.join(root, f)
            for root, _, files in os.walk(directory)
            for f in files)
        txtfileiter = (f for f in fileiter if os.path.splitext(f)[1] == '.'+extention)
        for txt in txtfileiter:
            print txt
            file_stuck.append(txt)
        print file_stuck



# shit.folder("\\\\nas\\Public\\QA\\AV_logs")
shit = function()
shit.download("ec2-54-69-155-182.us-west-2.compute.amazonaws.com",'?e=pcho&dd=3&sfx=2&mb=1&ne=1&jc=1')