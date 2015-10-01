__author__ = 'Robert Adinihy'

import Constans
import paramiko

class Builder_constructor:
    #Main costractor
    def __init__(self, brand, brand_c):
        #Type_lpo_Servers
        if brand == Constans.I_type1:
             self.brand_1 = Constans.I_type1
             self.brand_url_1 = Constans.Type_lpo_Servers
             self.brand_url_2 = Constans.Type_lpo_Servers1
             self.brand_url_3 = Constans.Type_lpo_Servers2
             self.brand_url_4 = Constans.Type_lpo_Servers3
             self.brand_url_5 = Constans.Type_lpo_Servers4


        #Type_FS_Servers
        elif brand == Constans.I_type:
            self.brand_1=Constans.I_type
            self.brand_url_1 = Constans.Type_FS_Servers1
            self.brand_url_2 = Constans.Type_FS_Servers11
            self.brand_url_3 = Constans.Type_FS_Servers2
            self.brand_url_4 = Constans.Type_FS_Servers3
            self.brand_url_5 = Constans.Type_FS_Servers4
        #Type_MB_Servers
        elif brand == Constans.I_type2:
            self.brand_1=Constans.I_type2
            self.brand_url_1 = Constans.Type_MB_Servers
            self.brand_url_6 = Constans.Type_lpo_Servers5
            self.brand_url_7 = Constans.Type_lpo_Servers6

        else:
             print "brand doesn't exsit"

        #bijo_copy
        if brand_c == Constans.brand_c_i:
            self.brand_c1=Constans.comand_i
            self.brand_c2=Constans.comand_i1
            self.brand_c3=Constans.comand_i11
        else:
            print "brand doesn't exsit"
    #conection&comand in sever
    def conection_run_comand(self, hostname_1, port_1, username_1, pw, command_1):

           if hostname_1 == '':
               bob ='not host'
               print 'not host'
           else:
                bob= 'host exsit'
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
                return bob
    #secons constractor
    def p(self):
      if self.brand_1 != Constans.I_type2:
        print self.brand_1
        print self.brand_url_1
        if self.brand_url_1=='':
            print "null"
        else:
            self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c1)
            self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c2)
            self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c3)
        print "######################################################################################"
        print self.brand_1
        print self.brand_url_2
        if self.brand_url_2=='':
            print "null"
        else:
            self.conection_run_comand(self.brand_url_2, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c1)
            self.conection_run_comand(self.brand_url_2, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c2)
            self.conection_run_comand(self.brand_url_2, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c3)
        print "######################################################################################"
        print self.brand_1
        print self.brand_url_3
        if self.brand_url_3 == '':
            print "null"
        else:
            self.conection_run_comand(self.brand_url_3, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c1)
            self.conection_run_comand(self.brand_url_3, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c2)
            self.conection_run_comand(self.brand_url_3, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c3)
        print "######################################################################################"

        print self.brand_1
        print self.brand_url_4
        if self.brand_url_4 == '':
            print "null"
        else:

            self.conection_run_comand(self.brand_url_4, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c1)
            self.conection_run_comand(self.brand_url_4, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c2)
            self.conection_run_comand(self.brand_url_4, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c3)
        print "######################################################################################"
        print self.brand_1
        print self.brand_url_5
        if self.brand_url_5 == '':
            print "null"
        else:
            self.conection_run_comand(self.brand_url_5, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c1)
            self.conection_run_comand(self.brand_url_5, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c2)
            self.conection_run_comand(self.brand_url_5, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c3)
        print "######################################################################################"





      else:
        print self.brand_1
        print self.brand_url_1

        if self.brand_url_1=='':
            print "null"
        else:
            self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c1)
            self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c2)
            self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c3)
        print "######################################################################################"

        print Constans.I_type1
        print self.brand_url_6
        if self.brand_url_6=='':
            print "null"
        else:
            self.conection_run_comand(self.brand_url_6, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c1)
            self.conection_run_comand(self.brand_url_6, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c2)
            self.conection_run_comand(self.brand_url_6, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c3)
        print "######################################################################################"

        print Constans.I_type1
        print self.brand_url_7
        if self.brand_url_7=='':
            print "null"
        else:
            self.conection_run_comand(self.brand_url_7, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c1)
            self.conection_run_comand(self.brand_url_7, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c2)
            self.conection_run_comand(self.brand_url_7, Constans.port, Constans.user, Constans.pw_i,
                                      self.brand_c3)
        print "######################################################################################"








