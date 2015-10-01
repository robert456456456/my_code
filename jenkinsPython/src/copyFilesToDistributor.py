#!/usr/bin/env python

# # Copy files unattended over SSH using a glob pattern.
# # It tries first to connect using a private key from a private key file
# # or provided by an SSH agent. If RSA authentication fails, then 
# # password login is attempted.

# #
# # DEPENDENT MODULES:
# #      * paramiko, install it with `easy_install paramiko`

# # NOTE: 1. The script assumes that the files on the source
# #       computer are *always* newer that on the target;
# #       2. no timestamps or file size comparisons are made
# #       3. use at your own risk

# hostname = '46.19.138.195' # remote hostname where SSH server is running
# port = 22
# username = 'root'
# password = 'Jen512625!!'
# rsa_private_key = r"/root/.ssh/id_rsa"
# nbytes = 4096
# max_num_files_to_copy = 100

dir_local = '/Storage/DEFENDER_SETUP_2013_PRODUCTION/'
dir_local_archive = '/Storage/DEFENDER_SETUP_2013_PRODUCTION_ARCHIVE/'
dir_remote = "/Storage/DEFENDER_SETUP_2013_PRODUCTION/"
glob_pattern = '*.dll'
rsa_private_key = r"/home/jenkins/.ssh/id_rsa"
# rsa_private_key = r"/root/.ssh/id_rsa"
nbytes = 4096

import os
import shutil
import sys
# import subprocess
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

def ssh_command(hostname, port, username, password, command):
    
    print "Execution of command ", command
     
    try:
        host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    except IOError:
        try:
            # try ~/ssh/ too, e.g. on windows
            host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
        except IOError:
            print '*** Unable to open host keys file'
            host_keys = {}
    
    if host_keys.has_key(hostname):
        hostkeytype = host_keys[hostname].keys()[0]
        hostkey = host_keys[hostname][hostkeytype]
        print 'Using host key of type %s' % hostkeytype
    
    # now, connect and use paramiko Transport to negotiate SSH2 across the connection
    try:
        trans = paramiko.Transport((hostname, port))
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

                print 'exit status: ', session.recv_exit_status()
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
    
    
    
    print 60 * "="



def main(argv):
    
    try:
        opts, args = getopt.getopt(argv, "h:p:u:a:m:", ["hostname=", "port=", "username=", "password=", "max_num_files_to_copy="])
    except getopt.GetoptError:
       print 'copyFilesToDistributor.py -h <hostname> -p <port> -u <username> -a <password> -m <max_num_files_to_copy>'
       sys.exit(2)
       
    for opt, arg in opts:
          if opt == '--help':
             print 'copyFilesToDistributor.py -h <hostname> -p <port> -u <username> -a <password> -m <max_num_files_to_copy>'
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
    # print "Port:", port
    print "Username:", username
    # print "Password: ", password
    print "Max num files to copy:", max_num_files_to_copy   
        
       

    # get host key, if we know one
    # rsa_private_key = r"/root/.ssh/id_rsa"
    nbytes = 4096

    hostkeytype = None
    hostkey = None
    files_copied = 0
    
    try:
        print "Hostname: ", hostname
        print "Port:", port
        print "Username:", username
        print "Password: ", password

        ssh_command(hostname, port, username, password, "pwd")
        # ssh_command("ls")
        # ssh_command("cd /Storage/DEFENDER_SETUP_2013_PRODUCTION/")
        ssh_command(hostname, port, username, password, "echo `ls -tr /Storage/DEFENDER_SETUP_2013_PRODUCTION/ | grep dll | tail -n 1` > /home/jenkins/latestfile")
        
    except:
        print "SSH command failed"
        
    try:
        host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    except IOError:
        try:
            # try ~/ssh/ too, e.g. on windows
            host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
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
    
        latestCopiedFileTimestamp = 0.0
         
        sftp.get("/home/jenkins/latestfile", "/home/jenkins/latestfile");
        fo = open("/home/jenkins/latestfile", "r+")
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
        files = [ f for f in files if re.search('.dll$', f, re.I)]
    
        print "Total number of DLL files in source directory ", dir_local, " is ", len(files)
        
        files.sort()
        oldFiles = 0
        newFiles = 0
        
        for file in files:
            if files_copied < max_num_files_to_copy:
                local_file = dir_local + file
                # filetime = localtime(filetimesecs)
                timediff = os.path.getmtime(local_file) - latestCopiedFileTimestamp
                # print "Filename: " , file , "time difference from latest copied file: ", timediff
                # print "Latest copied file timestamp is: %s" % (latestCopiedFileTimestamp)
                if timediff <= 0:
                    oldFiles += 1
                else:
                    newFiles += 1
                    try:
                        remote_file = dir_remote + file
                        print 'Copying file #', files_copied, ': ', remote_file
                        sftp.put(local_file, remote_file)
                        
                        # local_file_data = open(local_file, "rb").read()
                        # remote_file_data = sftp.open(remote_file)
                        # remote_file_stat = sftp.stat(remote_file)
                        # print "Remote file status: ", remote_file_stat
                        # md1 = hashlib.md5(local_file_data).hexdigest()
                        # print "Local file MD5: ", md1
                        
                        # md2 = hashlib.md5(remote_file_data).hexdigest()
                        # print "Remote file MD5: ", md2
                        # if md1 == md2:
                        try:
                            # os.system("sudo mv " + local_file + " " + dir_local_archive)
                            # subprocess.call(shutil.move(local_file, dir_local_archive)
                            shutil.move(local_file, dir_local_archive)
                        # except Exception, e1:
                        except:
                            print 'move file to archive failed'
                            # print '*** Caught exception: %s: %s' % (e1.__class__, e1)
                            
                        files_copied += 1
                        #    print '... succeeded'
                        # else:
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
    print "Old Files: ", oldFiles
    print "New Files: ", newFiles
    print 'Total files copied:', files_copied
    print 'All operations complete!'
    print '=' * 60

if __name__ == "__main__":
    main(sys.argv[1:])
