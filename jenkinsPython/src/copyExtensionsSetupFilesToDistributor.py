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
#port = 22
#username = 'root'
#password = 'Jen512625!!'
#rsa_private_key = r"/root/.ssh/id_rsa"
#nbytes = 4096
#max_num_files_to_copy = 100

dir_local='/Storage/EXTENSION_SETUP_2013_PRODUCTION/'
dir_remote = "/Storage/EXTENSION_SETUP_2013_PRODUCTION/"
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
    
def get_num_builds_on_distributor_in_server_mirror_directory(hostname,port,username,password,theSftp,server_id,server_ip,product_root_folder_name,product_name):
    num_builds_on_distributor_in_mirror = 0
    file_name_control_file = "num_"+product_name+"_files_on_distributor_in_mirror_"+server_ip
    directory_mirror_name = "/Storage/" + product_root_folder_name + "/" + server_ip
    try:
        ssh_command(hostname,port,username,password,"echo `ls " + directory_mirror_name + "/ | grep dll | wc -l` > /home/jenkins/" + file_name_control_file)
        theSftp.get("/home/jenkins/" + file_name_control_file,"/home/jenkins/" + file_name_control_file);
        fo_num_builds_on_distributor_in_mirror = open("/home/jenkins/" + file_name_control_file,"r+")
        #print "File is opened: ", fo_numFilesOnDistributorInBOX1.name
        s_num_builds_on_distributor_in_mirror = fo_num_builds_on_distributor_in_mirror.readline()
        if s_num_builds_on_distributor_in_mirror != None and s_num_builds_on_distributor_in_mirror:
            print "Number of builds On Distributor in " + directory_mirror_name + ": ", s_num_builds_on_distributor_in_mirror
            try:
                num_builds_on_distributor_in_mirror = int(s_num_builds_on_distributor_in_mirror.strip('\n'))
            except:
                print 'Empty value of number of ' + product_name + 'builds on Distributor in ' + directory_mirror_name
       
        fo_num_builds_on_distributor_in_mirror.close
    except Exception, e:
        print "Retrieving Number of " + product_name + "builds in " + directory_mirror_name + " failed"
        print '*** Caught exception: %s: %s' % (e.__class__, e)
       
    return num_builds_on_distributor_in_mirror

def get_distributor_server_locked(hostname,port,username,password,theSftp,server_id,server_ip,product_root_folder_path,product_name):
    file_name_control_file = "sync_"+product_name+"_" + server_ip + ".stat"
    directory_mirror_name = product_root_folder_path + server_ip

    try:
        ssh_command(hostname,port,username,password,"echo `ls " + directory_mirror_name + " | grep dll | wc -l` > /home/jenkins/" + file_name_control_file)
        theSftp.get("/home/jenkins/"+file_name_control_file,"/home/jenkins/"+file_name_control_file);
        fo_server_state = open("//home/jenkins/"+file_name_control_file,"r+")
        #print "File is opened: ", fo_numFilesOnDistributorInBOX1.name
        s_server_state = fo_server_state.readline()
        if s_server_state != None and s_server_state:
            print "State: server " + server_ip + " :", s_server_state
            if s_server_state == "syncronized":
                return 0
            else:
                print "State: server " + server_ip + " is not synchronized"
    except Exception, e:
        print "Retrieving State of server" + server_ip + " failed"
        print '*** Caught exception: %s: %s' % (e.__class__, e)
    return 1


def get_num_builds_on_distributor_in_product_directory(hostname,port,username,password,theSftp,product_root_folder_path,product_name):
    num_builds_on_distributor_in_product_directory = 0
    file_name_control_file = "num_"+product_name+"_files_on_distributor"
    directory_product_name = product_root_folder_path

    try:
        ssh_command(hostname,port,username,password,"echo `ls " + directory_product_name + " | grep dll | wc -l` > /home/jenkins/" + file_name_control_file)
        print '... 1'
        theSftp.get("/home/jenkins/" + file_name_control_file,"/home/jenkins/" + file_name_control_file);
        print '... 2'
        fo_num_builds_on_distributor_in_product_directory = open("/home/jenkins/" + file_name_control_file,"r+")
        #print "File is opened: ", fo_numFilesOnDistributorInGlobalDefenderDirectory.name
        print '... 3'
        s_num_builds_on_distributor_in_product_directory = fo_num_builds_on_distributor_in_product_directory.readline()
        print '... 4'
        if s_num_builds_on_distributor_in_product_directory != None and s_num_builds_on_distributor_in_product_directory:
            print '... 5'
            print "Number builds on Distributor in " + directory_product_name, s_num_builds_on_distributor_in_product_directory
            try:
                print '... 6'
                num_builds_on_distributor_in_product_directory = int(s_num_builds_on_distributor_in_product_directory.strip('\n'))
            except:
                print '... 7'
                print 'Empty value of number of ' + product_name + 'builds on Distributor in ' + directory_product_name
        print '... 8'
        fo_num_builds_on_distributor_in_product_directory.close
    except Exception, e1:
        print '... 9'
        print "Retrieving Number of " + product_name + "builds in " + directory_product_name + " failed"
        print '*** Caught exception: %s: %s' % (e1.__class__, e1)
        
    return num_builds_on_distributor_in_product_directory
        
def get_num_builds_on_distributor(hostname,port,username,password,theSftp,product_root_folder_path,product_name):
    
    total_num_builds_on_distributor_in_all_directories = 0
    num_builds_on_distributor_in_product_directory = get_num_builds_on_distributor_in_product_directory(hostname,port,username,password,theSftp,product_root_folder_path,product_name)
    num_builds_on_distributor_in_server_mirror_directory_162_210_193_205 = get_num_builds_on_distributor_in_server_mirror_directory(hostname,port,username,password,theSftp,1,"162.210.193.205",product_root_folder_path,product_name)
    num_builds_on_distributor_in_server_mirror_directory_162_210_193_208 = get_num_builds_on_distributor_in_server_mirror_directory(hostname,port,username,password,theSftp,2,"162.210.193.208",product_root_folder_path,product_name)
    num_builds_on_distributor_in_server_mirror_directory_91_109_18_40 = get_num_builds_on_distributor_in_server_mirror_directory(hostname,port,username,password,theSftp,3,"91.109.18.40",product_root_folder_path,product_name)
    num_builds_on_distributor_in_server_mirror_directory_95_211_187_166 = get_num_builds_on_distributor_in_server_mirror_directory(hostname,port,username,password,theSftp,4,"95.211.187.166",product_root_folder_path,product_name)
       
    total_num_builds_on_distributor_in_all_directories = \
        num_builds_on_distributor_in_product_directory + \
        num_builds_on_distributor_in_server_mirror_directory_162_210_193_205 + \
        num_builds_on_distributor_in_server_mirror_directory_162_210_193_208 + \
        num_builds_on_distributor_in_server_mirror_directory_91_109_18_40 + \
        num_builds_on_distributor_in_server_mirror_directory_95_211_187_166
        
    print "Total number of " + product_name + " builds on Distributor is " , total_num_builds_on_distributor_in_all_directories

    if total_num_builds_on_distributor_in_all_directories == 0:
        print "CARTRIDGE IS EMPTY"
        
    if total_num_builds_on_distributor_in_all_directories >= MAX_NUMBER_OF_FILES_ON_DISTRIBUTOR:
        print "CARTRIDGE IS FULL"
        
    return total_num_builds_on_distributor_in_all_directories

def main(argv):
    
    try:
        opts, args = getopt.getopt(argv,"h:p:u:a:b:m:",["hostname=","port=","username=","password=","build_branch=","number_of_builds="])
    except getopt.GetoptError:
       print 'copyExtensionsSetupFilesToDistributor.py -h <hostname> -p <port> -u <username> -a <password> -b <build_branch> -m <number_of_builds>'
       sys.exit(2)
       
    for opt, arg in opts:
          if opt == '--help':
             print 'copyExtensionsSetupFilesToDistributor.py -h <hostname> -p <port> -u <username> -a <password> -b <build_branch> -m <number_of_builds>'
             sys.exit()
          elif opt in ('-h', '--hostname'):
             hostname = str(arg)
          elif opt in ("-p", "--port"):
             port = int(arg)
          elif opt in ("-u", "--username"):
             username = str(arg)
          elif opt in ("-a", "--password"):
             password = str(arg)
          elif opt in ("-b", "--build_branch"):
             build_branch = str(arg)
          elif opt in ("-m", "--number_of_builds"):
             number_of_builds = int(arg)
             
          else:
              usage()
              sys.exit(2)
        
    #print "Hostname: ", hostname
    #print "Port:", port
    #print "Username:", username
    #print "Password: ", password
    #print "Build branch:",   build_branch 
    #print "Number of builds:",   number_of_builds    
        
    latestBuildsDirName =  "LATEST_" + str(number_of_builds)  
    
    product_name = "EXTENSION_SETUP_2013_PRODUCTION"
        
    product_root_folder_path = "/Storage/" + product_name + "/"
    
    product_root_branch_path = product_root_folder_path + "/" + build_branch + "/"


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
        
                
        total_num_builds_on_distributor = get_num_builds_on_distributor(hostname,port,username,password,theSftp,product_root_folder_path,product_name)
        
        if total_num_builds_on_distributor >= MAX_NUMBER_OF_FILES_ON_DISTRIBUTOR:
            return

        try:
            ssh_command(hostname,port,username,password,"echo `ls -ltr /Storage/EXTENSION_SETUP_2013_PRODUCTION/` > /home/jenkins/extensionSetupDirectoryContent")
        except:
            print "SSH command failed"
    
        build_branch_directory_exists = False 
        latest_builds_directory_exists = False
        
        sftp.get("/home/jenkins/extensionSetupDirectoryContent","/home/jenkins/extensionSetupDirectoryContent");
        
        for line in open("/home/jenkins/extensionSetupDirectoryContent","r+").readlines():
            #print line.strip()
            if latestBuildsDirName in line.strip():
                build_branch_directory_exists = True
            if latestBuildsDirName in line.strip():
                latest_builds_directory_exists = True
        
        if build_branch_directory_exists == False:
            try:
                ssh_command(hostname,port,username,password,"mkdir /Storage/EXTENSION_SETUP_2013_PRODUCTION/" + build_branch)
            except:
                print "SSH command failed"

            try:
                ssh_command(hostname,port,username,password,"echo `ls -ltr /Storage/EXTENSION_SETUP_2013_PRODUCTION/` > /home/jenkins/extensionSetupDirectoryContent")
            except:
                print "SSH command failed"

            for line in open("/home/jenkins/extensionSetupDirectoryContent","r+").readlines():
                #print line.strip()
                if build_branch in line.strip():
                    build_branch_directory_exists = True
            if build_branch_directory_exists == False:
                sys.exit(2)
        
        if latest_builds_directory_exists == False:
            try:
                ssh_command(hostname,port,username,password,"mkdir /Storage/EXTENSION_SETUP_2013_PRODUCTION/" + latestBuildsDirName)
            except:
                print "SSH command failed"

            try:
                ssh_command(hostname,port,username,password,"echo `ls -ltr /Storage/EXTENSION_SETUP_2013_PRODUCTION/` > /home/jenkins/extensionSetupDirectoryContent")
            except:
                print "SSH command failed"

            for line in open("/home/jenkins/extensionSetupDirectoryContent","r+").readlines():
                #print line.strip()
                if latestBuildsDirName in line.strip():
                    latest_builds_directory_exists = True
            if latest_builds_directory_exists == False:
                sys.exit(2)
 
 #   Rsync distributor
        os.system("rsync -avz -d --progress -e 'ssh -p 27628 -i /home/jenkins/.ssh/disterbutor' /Storage/EXTENSION_SETUP_2013_PRODUCTION/" + build_branch + "/ " + username + "@" + hostname + ":/Storage/EXTENSION_SETUP_2013_PRODUCTION/" + build_branch+"/")
        
        print 'Copy EXTENSIONS SETUP files to Distributor is completed' 
        
        try:
            ssh_command(hostname,port,username,password,"rm -rf /Storage/EXTENSION_SETUP_2013_PRODUCTION/" + latestBuildsDirName + "/*")
            print 'The directory /Storage/EXTENSION_SETUP_2013_PRODUCTION/' + latestBuildsDirName +' is cleaned'    
        except:
            print "SSH command failed"
        
        try:
            ssh_command(hostname,port,username,password,"ls -d -1 /Storage/EXTENSION_SETUP_2013_PRODUCTION/*/* | tail -250 | sort -r | while IFS='' read -r dir ; do cp -rf ""$dir"" /Storage/EXTENSION_SETUP_2013_PRODUCTION/" + latestBuildsDirName + "/ ; done;")
            print 'The directory /Storage/EXTENSION_SETUP_2013_PRODUCTION/' + latestBuildsDirName +' is refilled'
        except:
            print "SSH command failed"
        
        try:
            ssh_command(hostname,port,username,password,"ls -la /Storage/EXTENSION_SETUP_2013_PRODUCTION/" + latestBuildsDirName + "/ > /home/jenkins/latestBuildsDirContent")
        except:
            print "SSH command failed"

        sftp.get("/home/jenkins/latestBuildsDirContent","/home/jenkins/latestBuildsDirContent");
        
        print 'Content of the directory /Storage/EXTENSION_SETUP_2013_PRODUCTION/' + latestBuildsDirName
        
        for line in open("/home/jenkins/latestBuildsDirContent","r+").readlines():
            print line.strip()
    
    except Exception, e:
        print '*** Caught exception: %s: %s' % (e.__class__, e)
        try:
            t.close()
        except:
            pass

if __name__ == "__main__":
    main(sys.argv[1:])
