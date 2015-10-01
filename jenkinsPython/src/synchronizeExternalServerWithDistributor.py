#!/usr/bin/env python


dir_local='/Storage/EXTENSION_SETUP_2013_PRODUCTION/'
dir_remote = "/Storage/EXTENSION_SETUP_2013_PRODUCTION/"
rsa_private_key = r"/home/jenkins/.ssh/extension2"
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

def agent_auth(transport, username,rsa_private_key):

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


def simple_ssh_command(hostname,port,username,password,command,rsa_private_key):
   
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
 
    
def ssh_command(hostname,port,username,command,rsa_private_key):
    
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
    
def main(argv):
    
    try:
        opts, args = getopt.getopt(argv,"h:p:u:m:k:",["hostname=","port=","username=","number_of_builds=","ssh_key_path="])
    except getopt.GetoptError:
       print 'copyExtensionsSetupFilesToDistributor.py -h <hostname> -p <port> -u <username> -m <number_of_builds> -k <ssh_key_path>'
       sys.exit(2)
       
    for opt, arg in opts:
          if opt == '--help':
             print 'copyExtensionsSetupFilesToDistributor.py -h <hostname> -p <port> -u <username> -m <number_of_builds> -k <ssh_key_path>'
             sys.exit()
          elif opt in ('-h', '--hostname'):
             hostname = str(arg)
          elif opt in ("-p", "--port"):
             port = int(arg)
          elif opt in ("-u", "--username"):
             username = str(arg)
          elif opt in ("-m", "--number_of_builds"):
             number_of_builds = int(arg)
          elif opt in ("-k", "--ssh_key_path"):
             ssh_key_path = str(arg)
             
          else:
              usage()
              sys.exit(2)
        
    #print "Hostname: ", hostname
    #print "Port:", port
    #print "Username:", username
    #print "Password: ", password
    #print "Build branch:",   build_branch 
    #print "Number of builds:",   number_of_builds 
    print "ssh_key_path: ", ssh_key_path   
        
    latestBuildsDirName =  "LATEST_" + str(number_of_builds)  

    # get host key, if we know one
    rsa_private_key = ssh_key_path
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
        
        
    
        agent_auth(t, username,rsa_private_key)
        
        
    
        #if not t.is_authenticated():
        #    print 'RSA key auth failed! Trying password login...'
        #    t.connect(username=username, password=password)
        #else:
        sftp = t.open_session()
        sftp = paramiko.SFTPClient.from_transport(t)
                
 #   Rsync Remote Server against Distributor

        try:
            print "Start synchronization of directory /Compiled/EXTENSION_SETUP_2013_PRODUCTION/ on server " + hostname 
            commandToExecute = "rsync -aqz -d --progress -e 'ssh -p 27628 -i /home/jenkins/.ssh/disterbutor' jenkins@46.19.138.195:/Storage/EXTENSION_SETUP_2013_PRODUCTION/" + latestBuildsDirName + "/ /Compiled/EXTENSION_SETUP_2013_PRODUCTION/"
            ssh_command(hostname,port,username,commandToExecute,rsa_private_key)
            print "The directory /Compiled/EXTENSION_SETUP_2013_PRODUCTION/ is synchronized on server " + hostname    
        except Exception, e1:
            print "SSH command failed " + commandToExecute
            print '*** Caught exception: %s: %s' % (e1.__class__, e1)

             
        try:
            commandToExecute = "ls -1 /Compiled/EXTENSION_SETUP_2013_PRODUCTION/ > /home/jenkins/extensionsProductionZipDirContent"
            ssh_command(hostname,port,username,commandToExecute,rsa_private_key)
        except Exception, e2:
            print "SSH command failed: " + commandToExecute
            print '*** Caught exception: %s: %s' % (e2.__class__, e2)


        sftp.get("/home/jenkins/extensionsProductionZipDirContent","/home/jenkins/extensionsProductionZipDirContent");

        try:
            commandToExecute0 = 'DIRECTORIES=/Compiled/EXTENSION_SETUP_2013_PRODUCTION/*;' + \
            'for f in $DIRECTORIES; do' + \
            ' RESULT="${f##*/}";'+\
            ' if [ ! -d /Extracted/EXTENSION_SETUP_2013_PRODUCTION/$RESULT ];' + \
            ' then mkdir /Extracted/EXTENSION_SETUP_2013_PRODUCTION/$RESULT;' + \
            'fi;'+\
            'if [ -f /Compiled/EXTENSION_SETUP_2013_PRODUCTION/$RESULT/recompileBinaries.tar.gz ];' + \
            ' then cd /Compiled/EXTENSION_SETUP_2013_PRODUCTION/$RESULT/;' + \
            ' tar -zxvf /Compiled/EXTENSION_SETUP_2013_PRODUCTION/$RESULT/recompileBinaries.tar.gz;' + \
            ' mv /Compiled/EXTENSION_SETUP_2013_PRODUCTION/$RESULT/*/* /Extracted/EXTENSION_SETUP_2013_PRODUCTION/$RESULT;' + \
            'fi;' + \
            'done;'
            
            ssh_command(hostname,port,username,commandToExecute0,rsa_private_key)
        except Exception, e10:
            print "SSH command failed: " + commandToExecute0
            print '*** Caught exception: %s: %s' % (e10.__class__, e10)
        
        print "Content of the directory /Compiled/EXTENSION_SETUP_2013_PRODUCTION/ on server " + hostname
        
        for line in open("/home/jenkins/extensionsProductionZipDirContent","r+").readlines():
            print line.strip()
            #try:
            #    commandToExtract1= 'cd /Compiled/EXTENSION_SETUP_2013_PRODUCTION/'+line.strip()+';result="${PWD##*/}";if [ ! -d /Extracted/EXTENSION_SETUP_2013_PRODUCTION/$result ]; then mkdir /Extracted/EXTENSION_SETUP_2013_PRODUCTION/$result;fi'
            #    ssh_command(hostname,port,username,commandToExtract1,rsa_private_key)
            #    try:
            #        commandToExtract2='cd /Compiled/EXTENSION_SETUP_2013_PRODUCTION/'+line.strip()+';result="${PWD##*/}";if [ -f recompileBinaries.tar.gz ]; then tar -zxvf recompileBinaries.tar.gz; mv ./*/* /Extracted/EXTENSION_SETUP_2013_PRODUCTION/$result;fi'
            #        ssh_command(hostname,port,username,commandToExtract2,rsa_private_key)
            #    except Exception, e5:
            #        print "SSH command failed: " + commandToExtract2
            #        print '*** Caught exception: %s: %s' % (e5.__class__, e5)    
            #except Exception, e4:
            #    print "SSH command failed: " + commandToExtract1
            #    print '*** Caught exception: %s: %s' % (e4.__class__, e4)
            
    # Extract TAR.GZ files on Remote Server
        try:
            commandToExecute = "ls -R /Extracted/EXTENSION_SETUP_2013_PRODUCTION/ > /home/jenkins/extensionsProductionExtractedDirContent"
            ssh_command(hostname,port,username,commandToExecute,rsa_private_key)
        except Exception, e3:
            print "SSH command failed: " + commandToExecute
            print '*** Caught exception: %s: %s' % (e3.__class__, e3)

        sftp.get("/home/jenkins/extensionsProductionExtractedDirContent","/home/jenkins/extensionsProductionExtractedDirContent");
        
        print "Content of the directory /Extracted/EXTENSION_SETUP_2013_PRODUCTION/ on server " + hostname
        
        for line1 in open("/home/jenkins/extensionsProductionExtractedDirContent","r+").readlines():
            print line1.strip()

    except Exception, e:
        print '*** Caught exception: %s: %s' % (e.__class__, e)
        try:
            t.close()
        except:
            pass
        
#   Rsync server 1 with distributor
    

if __name__ == "__main__":
    main(sys.argv[1:])
