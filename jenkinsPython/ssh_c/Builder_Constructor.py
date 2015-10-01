__author__ = 'Robert Adinihy'

import Constans
import paramiko

class Builder_constructor:
    #Main costractor
    def __init__(self, brand, brand_c):
        #Main
        if brand == Constans.Brand_Main:
             self.brand_1 = Constans.Brand_Main
             self.brand_url_1 = Constans.Main_Builder_url
        #Fallback_1
        elif brand == Constans.Brand_Fallback_1:
            self.brand_1=Constans.Brand_Fallback_1
            self.brand_url_1 = Constans.Fallback_1_Builder_url
        #Fallback_2
        elif brand == Constans.Brand_Fallback_2:
            self.brand_1 = Constans.Brand_Fallback_2
            self.brand_url_1 = Constans.Fallback_2_Builder_url
        #Panda_1
        elif brand == Constans.Brand_Panda_1:
            self.brand_1 = Constans.Brand_Panda_1
            self.brand_url_1=Constans.Panda_1_Builder_url
        #Panda_2
        elif brand == Constans.Brand_Panda_2:
            self.brand_1 = Constans.Brand_Panda_2
            self.brand_url_1=Constans.Panda_2_Builder_url
        #Zet
        elif brand == Constans.Brand_Zet:
            self.brand_1=Constans.Brand_Zet
            self.brand_url_1=Constans.Zet_Builder_url
        #MD
        elif brand == Constans.Brand_Media_Buying:
            self.brand_1=Constans.Brand_Media_Buying
            self.brand_url_1 = Constans.Media_Buying_Builder_url
        #Primary_Update
        elif brand == Constans.Brand_Primary_Update:
            self.brand_1 = Constans.Brand_Primary_Update
            self.brand_url_1 = Constans.Primary_Update_Builder_url
        #Teddy
        elif brand == Constans.Brand_Teddy:
            self.brand_1 = Constans.Brand_Teddy
            self.brand_url_1 = Constans.Teddy_Builder_url
        else:
             print "brand doesn't exsit"
        #add new comands brand_co
        #bijo_copy
        if brand_c == Constans.brand_c_bi:
            self.brand_c8=Constans.brand_c_bi
            self.brand_c1=Constans.comand_bi_r
            self.brand_c2=Constans.comand_bi_c
        #BHO_copy
        elif brand_c == Constans.brand_c_bh:
            self.brand_c8=Constans.brand_c_bh
            self.brand_c1=Constans.comand_bh_r
            self.brand_c2=Constans.comand_bh_r1
            self.brand_c3=Constans.comand_bh_r2
            self.brand_c4=Constans.comand_bh_c
            self.brand_c5=Constans.comand_bh_c1
            self.brand_c6=Constans.comand_bh_c2
        #BHO_Uninstuller
        elif brand_c == Constans.brand_c_un:
            self.brand_c8= Constans.brand_c_un
            self.brand_c1=Constans.comand_bhu_r
            self.brand_c2=Constans.comand_bhu_c
        #Firefox_silicon_copy
        elif brand_c == Constans.brand_c_ff:
            self.brand_c8=Constans.brand_c_ff
            self.brand_c1=Constans.comand_f_r
            self.brand_c2=Constans.comand_f_c
        #Copy_all_components
        elif brand_c == Constans.brand_c_al:
            self.brand_c8=Constans.brand_c_al
            self.brand_c1=Constans.comand_bi_r
            self.brand_c2=Constans.comand_bi_c
        else:
            print "brand doesn't exsit"
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
            return "end operation"
    #secons constractor
    def p(self):

      if self.brand_c8 != Constans.brand_c_bh:


          print 'no bho'
          print 'brannd'+self.brand_1
          self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw,
                                      self.brand_c1)
          self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw,
                                      self.brand_c2)
      else:
        print "yes bho"
        print self.brand_1
        self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw,
                                  self.brand_c1)
        self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw,
                                  self.brand_c2)
        self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw,
                                  self.brand_c3)
        self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw,
                                  self.brand_c4)
        self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw,
                                  self.brand_c5)
        self.conection_run_comand(self.brand_url_1, Constans.port, Constans.user, Constans.pw,
                                  self.brand_c6)






