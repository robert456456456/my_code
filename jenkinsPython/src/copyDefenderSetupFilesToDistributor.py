#!/usr/bin/env python

## Copy files unattended over SSH using a glob pattern.
## It tries first to connect using a private key from a private key file
## or provided by an SSH agent. If RSA authentication fails, then 
## password login is attempted.

##
## DEPENDENT MODULES:
##      * paramiko, install it with `easy_install paramiko`

## NOTE: 1. The script assumes that the files on the source
##       computer are *always* newer that on the target;
##       2. no timestamps or file size comparisons are made
##       3. use at your own risk

#hostname = '46.19.138.195' # remote hostname where SSH server is running
#port = 27628
#username = 'root'
#password = 'Jen512625!!'
#rsa_private_key = r"/root/.ssh/id_rsa"
#nbytes = 4096
#max_num_files_to_copy = 100

dir_local='/Storage/DEFENDER_SETUP_2013_PRODUCTION/'
dir_local_archive='/Storage/DEFENDER_SETUP_2013_PRODUCTION_ARCHIVE/'
dir_remote = "/Storage/DEFENDER_SETUP_2013_PRODUCTION/"
glob_pattern='*.dll'
rsa_private_key = r"/home/jenkins/.ssh/id_rsa"
#rsa_private_key = r"/root/.ssh/id_rsa"
nbytes = 4096
MAX_NUMBER_OF_FILES_ON_DISTRIBUTOR = 100000

import os
import shutil
import sys
#import subprocess,getpass
import getopt
import glob
import paramiko
import hashlib
from datetime import date, timedelta, datetime
from time import localtime
import re

def agent_auth(transport, username):

    """
    Attempt to authenticate to the given transport using any of the private
    keys available from an SSH agent or from a local private RSA key file (assumes no pass phrase).
    """
    try:
        ki = paramiko.RSAKey.from_private_key_file(rsa_private_key)
    except Exception, e:
        print 'Failed loading' % (rsa_private_key, e)

    agent = paramiko.Agent()
    agent_keys = agent.get_keys() + (ki,)
    if len(agent_keys) == 0:
        return

    for key in agent_keys:
        print 'Trying ssh-agent key %s' % key.get_fingerprint().encode('hex'),
        try:
            transport.auth_publickey(username, key)
            print '... success!'
            return
        except paramiko.SSHException, e:
            print '... failed!', e


def simple_ssh_command(hostname,port,username,password,command):
   
    #print "Execution of command ", command
    try:

        t = paramiko.Transport((hostname,port))
        t.start_client()
        t.auth_password(username=username, password=password)
        
        session = t.open_channel("session")
        stdout_data = []
        stderr_data = []
                
        session.exec_command(command)

        while True:
            if session.recv_ready():
                stdout_data.append(session.recv(nbytes))
            if session.recv_stderr_ready():
                stderr_data.append(session.recv_stderr(nbytes))
            if session.exit_status_ready():
                break

        #print 'exit status: ', session.recv_exit_status()
        print ''.join(stdout_data)
        print ''.join(stderr_data)
      
        session.close()
                 
    except paramiko.SSHException, e:
        print '... failed!', e
    try:
        t.close()
    except:
        pass
 
    
def ssh_command(hostname,port,username,password,command):
    
    #print "Execution of command ", command
     
    try:
        host_keys = paramiko.util.load_host_keys(os.path.expanduser('/home/jenkins/.ssh/known_hosts'))
    except IOError:
        try:
            # try ~/ssh/ too, e.g. on windows
            host_keys = paramiko.util.load_host_keys(os.path.expanduser('/home/jenkins/ssh/known_hosts'))
        except IOError:
            print '*** Unable to open host keys file'
            host_keys = {}
    
    if host_keys.has_key(hostname):
        hostkeytype = host_keys[hostname].keys()[0]
        hostkey = host_keys[hostname][hostkeytype]
        print 'Using host key of type %s' % hostkeytype
    
    # now, connect and use paramiko Transport to negotiate SSH2 across the connection
    try:
        trans = paramiko.Transport((hostname,port))
        trans.start_client()
        try:
            ki = paramiko.RSAKey.from_private_key_file(rsa_private_key)
        except Exception, e:
            print 'Failed loading' % (rsa_private_key, e)

        agent = paramiko.Agent()
        agent_keys = agent.get_keys() + (ki,)
        if len(agent_keys) == 0:
            return

        for key in agent_keys:
            print 'Trying ssh-agent key %s' % key.get_fingerprint().encode('hex'),
            try:
                trans.auth_publickey(username, key)
                print '... success!'
                session = trans.open_channel("session")
                stdout_data = []
                stderr_data = []
                
                session.exec_command(command)
                while True:
                    if session.recv_ready():
                        stdout_data.append(session.recv(nbytes))
                    if session.recv_stderr_ready():
                        stderr_data.append(session.recv_stderr(nbytes))
                    if session.exit_status_ready():
                        break

                #print 'exit status: ', session.recv_exit_status()
                print ''.join(stdout_data)
                print ''.join(stderr_data)
                
                session.close()
                
            except paramiko.SSHException, e:
                print '... failed!', e
        try:
            trans.close()
        except:
            pass
        
    except:
        print "SSH connect failed"
    
    #print 60*"="
    
def getDistributorBox1Capacity(hostname,port,username,password,theSftp):
    numFilesOnDistributorInBOX1 = 0
    try:
        ssh_command(hostname,port,username,password,"echo `ls /Storage/DEFENDER_SETUP_2013_PRODUCTION/BOX1/ | grep dll | wc -l` > /home/jenkins/numDefenderSetupFilesOnDistributorInBOX1")
        theSftp.get("/home/jenkins/numDefenderSetupFilesOnDistributorInBOX1","/home/jenkins/numDefenderSetupFilesOnDistributorInBOX1");
        fo_numFilesOnDistributorInBOX1 = open("/home/jenkins/numDefenderSetupFilesOnDistributorInBOX1","r+")
        #print "File is opened: ", fo_numFilesOnDistributorInBOX1.name
        s_numFilesOnDistributorInBOX1 = fo_numFilesOnDistributorInBOX1.readline()
        if s_numFilesOnDistributorInBOX1 != None and s_numFilesOnDistributorInBOX1:
            print "Number Files On Distributor in DEFENDER SETUP BOX1 Directory is: ", s_numFilesOnDistributorInBOX1
            try:
                numFilesOnDistributorInBOX1 = int(s_numFilesOnDistributorInBOX1.strip('\n'))
            except:
                print 'Empty value of Number of DEFENDER SETUP Files On Distributor in BOX1'
       
        fo_numFilesOnDistributorInBOX1.close
    except:
        print "Retrieving Number of DEFENDER SETUP Files On BOX1 failed"
    return numFilesOnDistributorInBOX1

def getDistributorBoxLocked(hostname,port,username,password,theSftp,boxId):
    try:
        theSftp.get("/Storage/DEFENDER_SETUP_2013_PRODUCTION/sync_defender_box" + boxId + ".stat","/home/jenkins/sync_defender_box" + boxId + ".stat");
        fo_BOX_state = open("/home/jenkins/sync_defender_box" + boxId + ".stat","r+")
        #print "File is opened: ", fo_numFilesOnDistributorInBOX1.name
        s_BOX_state = fo_BOX_state.readline()
        if s_BOX_state != None and s_BOX_state:
            print "State: BOX" + boxId + " :", s_BOX_state
            if s_BOX_state == "syncronized":
                return 0
    except:
        print "Retrieving State of BOX" + boxId + " failed"
    return 1

def getDistributorBox2Capacity(hostname,port,username,password,theSftp):
    numFilesOnDistributorInBOX2 = 0
    try:
        ssh_command(hostname,port,username,password,"echo `ls /Storage/DEFENDER_SETUP_2013_PRODUCTION/BOX2/ | grep dll | wc -l` > /home/jenkins/numDefenderSetupFilesOnDistributorInBOX2")
        theSftp.get("/home/jenkins/numDefenderSetupFilesOnDistributorInBOX2","/home/jenkins/numDefenderSetupFilesOnDistributorInBOX2");
        fo_numFilesOnDistributorInBOX2 = open("/home/jenkins/numDefenderSetupFilesOnDistributorInBOX2","r+")
        #print "File is opened: ", fo_numFilesOnDistributorInBOX2.name
        s_numFilesOnDistributorInBOX2 = fo_numFilesOnDistributorInBOX2.readline()
        if s_numFilesOnDistributorInBOX2 != None and s_numFilesOnDistributorInBOX2:
            print "Number Files On Distributor in DEFENDER SETUP BOX2 Directory is: ", s_numFilesOnDistributorInBOX2
            try:
                numFilesOnDistributorInBOX2 = int(s_numFilesOnDistributorInBOX2.strip('\n'))
            except:
                print 'Empty value of Number of DEFENDER SETUP Files On Distributor in BOX2'
        
        fo_numFilesOnDistributorInBOX2.close
    except:
        print "Retrieving Number of DEFENDER SETUP Files On BOX2 failed"
    return numFilesOnDistributorInBOX2

def getDistributorBox3Capacity(hostname,port,username,password,theSftp):
    numFilesOnDistributorInBOX3 = 0
    try:
        ssh_command(hostname,port,username,password,"echo `ls /Storage/DEFENDER_SETUP_2013_PRODUCTION/BOX3/ | grep dll | wc -l` > /home/jenkins/numDefenderSetupFilesOnDistributorInBOX3")
        theSftp.get("/home/jenkins/numDefenderSetupFilesOnDistributorInBOX3","/home/jenkins/numDefenderSetupFilesOnDistributorInBOX3");
        fo_numFilesOnDistributorInBOX3 = open("/home/jenkins/numDefenderSetupFilesOnDistributorInBOX3","r+")
        #print "File is opened: ", fo_numFilesOnDistributorInBOX3.name
        s_numFilesOnDistributorInBOX3 = fo_numFilesOnDistributorInBOX3.readline()
        if s_numFilesOnDistributorInBOX3 != None and s_numFilesOnDistributorInBOX3:
            print "Number Files On Distributor in DEFENDER SETUP BOX3 Directory is: ", s_numFilesOnDistributorInBOX3
            try:
                numFilesOnDistributorInBOX3 = int(s_numFilesOnDistributorInBOX3.strip('\n'))
            except:
                print 'Empty value of Number of DEFENDER SETUP Files On Distributor in BOX3'
        
        fo_numFilesOnDistributorInBOX3.close
    except:
        print "Retrieving Number of DEFENDER SETUP Files On BOX3 failed"
    return numFilesOnDistributorInBOX3

def getDistributorGlobalDirectoryCapacity(hostname,port,username,password,theSftp):
    numFilesOnDistributorInGlobalDefenderDirectory = 0
    try:
        ssh_command(hostname,port,username,password,"echo `ls /Storage/DEFENDER_SETUP_2013_PRODUCTION/ | grep dll | wc -l` > /home/jenkins/numFilesOnDistributorInGlobalDefenderDirectory")
        print '... 1'
        theSftp.get("/home/jenkins/numFilesOnDistributorInGlobalDefenderDirectory","/home/jenkins/numFilesOnDistributorInGlobalDefenderDirectory");
        print '... 2'
        fo_numFilesOnDistributorInGlobalDefenderDirectory = open("/home/jenkins/numFilesOnDistributorInGlobalDefenderDirectory","r+")
        #print "File is opened: ", fo_numFilesOnDistributorInGlobalDefenderDirectory.name
        print '... 3'
        s_numFilesOnDistributorInGlobalDefenderDirectory = fo_numFilesOnDistributorInGlobalDefenderDirectory.readline()
        print '... 4'
        if s_numFilesOnDistributorInGlobalDefenderDirectory != None and s_numFilesOnDistributorInGlobalDefenderDirectory:
            print '... 5'
            print "Number Files On Distributor In Global Defender Directory is: ", s_numFilesOnDistributorInGlobalDefenderDirectory
            try:
                print '... 6'
                numFilesOnDistributorInGlobalDefenderDirectory = int(s_numFilesOnDistributorInGlobalDefenderDirectory.strip('\n'))
            except:
                print '... 7'
                print 'Empty value of Number Files On Distributor in Global Defender Directory'
        print '... 8'
        fo_numFilesOnDistributorInGlobalDefenderDirectory.close
    except Exception, e1:
        print '... 9'
        print "Retrieving Number Files On Distributor In Global Defender Directory failed"
        print '*** Caught exception: %s: %s' % (e1.__class__, e1)
        
    return numFilesOnDistributorInGlobalDefenderDirectory
        
def getDistributorCapacity(hostname,port,username,password,theSftp):
    
    totalNumFilesOnDistributorInDefenderDirectories = 0
    numFilesOnDistributorInGlobalDefenderDirectory = getDistributorGlobalDirectoryCapacity(hostname,port,username,password,theSftp)
    numFilesOnDistributorInBOX1 = getDistributorBox1Capacity(hostname,port,username,password,theSftp)
    numFilesOnDistributorInBOX2 = getDistributorBox2Capacity(hostname,port,username,password,theSftp)
    numFilesOnDistributorInBOX3 = getDistributorBox3Capacity(hostname,port,username,password,theSftp)
       
    totalNumFilesOnDistributorInDefenderDirectories = numFilesOnDistributorInGlobalDefenderDirectory + numFilesOnDistributorInBOX1 + numFilesOnDistributorInBOX2 + numFilesOnDistributorInBOX3
    print "Total Number Files On Distributor in Defender Directory is" , totalNumFilesOnDistributorInDefenderDirectories

    if totalNumFilesOnDistributorInDefenderDirectories == 0:
        print "CARTRIDGE IS EMPTY"
        
    if totalNumFilesOnDistributorInDefenderDirectories >= MAX_NUMBER_OF_FILES_ON_DISTRIBUTOR:
        print "CARTRIDGE IS FULL"
        
    return totalNumFilesOnDistributorInDefenderDirectories

def main(argv):
    
    try:
        opts, args = getopt.getopt(argv,"h:p:u:a:m:",["hostname=","port=","username=","password=","max_num_files_to_copy="])
    except getopt.GetoptError:
       print 'copyDefenderSetupFilesToDistributor.py -h <hostname> -p <port> -u <username> -a <password> -m <max_num_files_to_copy>'
       sys.exit(2)
       
    for opt, arg in opts:
          if opt == '--help':
             print 'copyDefenderSetupFilesToDistributor.py -h <hostname> -p <port> -u <username> -a <password> -m <max_num_files_to_copy>'
             sys.exit()
          elif opt in ('-h', '--hostname'):
             hostname = str(arg)
          elif opt in ("-p", "--port"):
             port = int(arg)
          elif opt in ("-u", "--username"):
             username = str(arg)
          elif opt in ("-a", "--password"):
             password = str(arg)
          elif opt in ("-m", "--max_num_files_to_copy"):
             max_num_files_to_copy = int(arg)
          else:
              usage()
              sys.exit(2)
        
    print "Hostname: ", hostname
    #print "Port:", port
    print "Username:", username
    #print "Password: ", password
    print "Max num files to copy:",   max_num_files_to_copy   
        
       

    # get host key, if we know one
    #rsa_private_key = r"/root/.ssh/id_rsa"
    nbytes = 4096

    hostkeytype = None
    hostkey = None
    files_copied = 0
    

        
        
    try:
        host_keys = paramiko.util.load_host_keys(os.path.expanduser('/home/jenkins/.ssh/known_hosts'))
    except IOError:
        try:
            # try ~/ssh/ too, e.g. on windows
            host_keys = paramiko.util.load_host_keys(os.path.expanduser('/home/jenkins/ssh/known_hosts'))
        except IOError:
            print '*** Unable to open host keys file'
            host_keys = {}
    
    if host_keys.has_key(hostname):
        hostkeytype = host_keys[hostname].keys()[0]
        hostkey = host_keys[hostname][hostkeytype]
        print 'Using host key of type %s' % hostkeytype
    
    # now, connect and use paramiko Transport to negotiate SSH2 across the connection
    try:
        print 'Establishing SSH connection to:', hostname, port, '...'
        
        t = paramiko.Transport((hostname, port))
        t.start_client()
        
        
    
        agent_auth(t, username)
        
        
    
        if not t.is_authenticated():
            print 'RSA key auth failed! Trying password login...'
            t.connect(username=username, password=password)
        else:
            sftp = t.open_session()
        sftp = paramiko.SFTPClient.from_transport(t)
                
        totalFilesOnDistributor = getDistributorCapacity(hostname,port,username,password,sftp)
        
        if totalFilesOnDistributor >= MAX_NUMBER_OF_FILES_ON_DISTRIBUTOR:
            return

        try:
            ssh_command(hostname,port,username,password,"echo `ls -tr /Storage/DEFENDER_SETUP_2013_PRODUCTION/ | grep dll | tail -n 1` > /home/jenkins/latestDefenderSetupFile")
        except:
            print "SSH command failed"
    
        latestCopiedFileTimestamp = 0.0
         
        sftp.get("/home/jenkins/latestDefenderSetupFile","/home/jenkins/latestDefenderSetupFile");
        fo = open("/home/jenkins/latestDefenderSetupFile","r+")
        print "File is opened: ", fo.name
        latestCopiedFile = fo.readline()
          
        if latestCopiedFile != None and latestCopiedFile:
            print "Latest copied file is: ", latestCopiedFile
            try:
                latestCopiedFileTimestamp = os.path.getmtime(latestCopiedFile.strip('\n'))
            except:
                print 'Empty file name'

    
        
        print "Latest copied file timestamp is: %s" % (latestCopiedFileTimestamp)
        fo.close
    
        files = os.listdir(dir_local)
        files = [ f for f in files if re.search('.dll$',f,re.I)]
    
        print "Total number of DLL files in source directory ", dir_local, " is ", len(files)
        
        files.sort()
        oldFiles = 0
        newFiles = 0
        
        for file in files:
            if files_copied < max_num_files_to_copy:
                local_file = dir_local + file
                #filetime = localtime(filetimesecs)
                timediff = os.path.getmtime(local_file) - latestCopiedFileTimestamp
            	#print "Filename: " , file , "time difference from latest copied file: ", timediff
                #print "Latest copied file timestamp is: %s" % (latestCopiedFileTimestamp)
                if timediff <= 0:
                    oldFiles += 1
                else:
                    newFiles += 1
                    try:
                        remote_file = dir_remote + file
                        
                        print 'Copying file #', files_copied, ': ', remote_file
                        
                        sftp.put(local_file, remote_file)
                        
                        #ssh_command(hostname,port,username,password,"ls -la " + remote_file)
                      
                        #local_file_data = open(local_file, "rb").read()
                        #remote_file_data = sftp.open(remote_file)
                        #remote_file_stat = sftp.stat(remote_file)
                        #print "Remote file status: ", remote_file_stat
                        #md1 = hashlib.md5(local_file_data).hexdigest()
                        #print "Local file MD5: ", md1
                        
                        #md2 = hashlib.md5(remote_file_data).hexdigest()
                        #print "Remote file MD5: ", md2
                        #if md1 == md2:
                        try:
                            #os.system("sudo mv " + local_file + " " + dir_local_archive)
                            #sudoPassword=getpass.getpass()
                            sudoPassword = 'Go512625'
                            simple_ssh_command('192.168.239.195',27628,'root',sudoPassword,'mv ' + local_file + ' ' + dir_local_archive)
                            #proc = subprocess.Popen(
                            #    ['sudo','-p','','-S','echo','mv ' + local_file + ' ' + dir_local_archive],
                            #    stdin=subprocess.PIPE)
                            #proc.stdin.write(sudoPassword+'\n')
                            #proc.stdin.close()
                            #proc.wait()
                            
                            #subprocess.call(shutil.move(local_file, dir_local_archive)
                            #shutil.copy(local_file, dir_local_archive)
                        #except Exception, e1:
                        except:
                            print 'Move file to archive failed'
                            #print '*** Caught exception: %s: %s' % (e1.__class__, e1)
                            
                        files_copied += 1
                        #    print '... succeeded'
                        #else:
                        #    print '... failed'
                    except Exception, e:
                        t.close()
                        raise
          
                  
    
    except Exception, e:
        print '*** Caught exception: %s: %s' % (e.__class__, e)
        try:
            t.close()
        except:
            pass
        
    print '=' * 60
    print 'Copy DEFENDER SETUP files to Distributor is completed'
    print "Old Files: ", oldFiles
    print "New Files: ", newFiles
    print 'Total files copied:',files_copied
    
    print '=' * 60
    print 'Distributor: distribution of DEFENDER SETUP files to images of BOXes'
    try:
        ssh_command(hostname,port,username,password,"/home/jenkins/distributeDefenderSetupFilesInsideDistributor.py")
    except:
        print "SSH command failed"
        
    print '=' * 60
   

    print 'All operations complete!'
   

if __name__ == "__main__":
    main(sys.argv[1:])
