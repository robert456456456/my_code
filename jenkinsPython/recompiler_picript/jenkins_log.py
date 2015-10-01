__author__ = 'root'
import Constans
import paramiko
class jenkins_log:
     #conection&comand in sever
    def conection_run_comand(self, hostname_1, port_1, username_1, pw, command_1):
            nbytes = 4096
            hostname = hostname_1
            port = port_1
            username = username_1
            password = pw
            command = command_1

            client = paramiko.Transport((hostname, port))
            client.connect(username=username, password=password)

            stdout_data = []
            stderr_data = []
            session = client.open_channel(kind='session')
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
            client.close()
    def clear(self,output):
        f = open(output,'w')
        f.write("") # python will convert \n to os.linesep
        f.close()

    def location(self,main,sub,output):
        with open(main, 'r') as content_file:
          content = content_file.read().splitlines()
        print content[0]+sub
        source=content[0]+sub
        f = open(output,'a')
        f.write(source+'\n') # python will convert \n to os.linesep
        f.close()

#jenkins_log().conection_run_comand(Constans.QA_Builder_url,Constans.port,Constans.user,Constans.pw,Constans.comand_i)
#jenkins_log().clear(Constans.Output_location)
#jenkins_log().location(Constans.Main_location_bho,Constans.Sub_loction_BHO1,Constans.Output_location)
#jenkins_log().location(Constans.Main_location_bho,Constans.Sub_loction_BHO2,Constans.Output_location)