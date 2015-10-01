__author__ = 'Robert Adinihy'
import Constans
import distutils.core
import os
import datetime
import stat
import glob
import shutil
import subprocess
from subprocess import Popen
class op:
    dest_p=""
    sub_dest=""
    s1=""
    s2=""
    def get_sores_location(self,location,count):
          with open(location, 'r') as content_file:
             content = content_file.read().splitlines()
             print content[count]


          return content[count]

    def loction_defition(self, sours, dest,exstention):
        """

        :rtype : object
        """
        with open(sours, 'r') as content_file:
            content = content_file.read().splitlines()

        source="/nas/"+content[0] + exstention
        f = open(dest, 'w')
        f.write(source+'\n') # python will convert \n to os.linesep
        f.close()


    def delet_copy(self, source, dest):
        #folder = 'd:\\BHO\\2015-02-25'
        folder = source
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception, e:
                print e

        source=source
        print source
        #dest='d:\\BHO\\2015-02-25\\'
        dest=dest
        print dest
        #shutil.copy2(source,dest)
        distutils.dir_util.copy_tree(source,dest)

    def copy_file_extention(self,folder1,folder,extention):
        dira = folder1
        dirb = folder

        for filename in glob.glob(os.path.join(dira,"*"+extention)):
           print os.path.join(dirb,os.path.basename(filename))
           if not os.path.isfile(os.path.join(dirb,os.path.basename(filename))):
               shutil.copy(filename,dirb)
    def write_to_file(self,output,cotent):
        f = open(output,'w')
        f.write(cotent) # python will convert \n to os.linesep
        f.close()

    def get_des_location(self,path,bat_l,otput_txt_name,Output_location):
        today = datetime.date.today()
        fullpath = os.path.join(path,str(today))
        print fullpath
        self.dest_p=fullpath+'\\'
        print self.dest_p
        self.s1=self.get_sores_location(Output_location,0)
        self.delet_copy(self.s1,self.dest_p)
        self.copy_file_extention(Constans.BHO_bat_l,self.dest_p,Constans.extention_b)
        self.write_to_file(bat_l+'\\'+otput_txt_name,self.dest_p)


    def muve_f(self,src,dest):
        path = src+"\\"
        files = os.listdir(path)
        files.sort()
        print files
        for f in files:
            src = path+f
            dst = dest+"\\"+f
            shutil.move(src, dst)



        '''
        fullpath = fullpath.replace('\n', '')
       ##create a tlb to hold the deleted files
        sub_path = os.path.join(fullpath, sub_path)
        print sub_path
        if not os.path.exists(sub_path):
                    os.makedirs(sub_path)
                    os.chmod(sub_path, stat.S_IWRITE)

                    self.sub_dest=sub_path+'\\'
                    print self.sub_dest
                    bob=self.sub_dest+'\\'
                    print bob+'bob'
                    self.s2=self.get_sores_location(Constans.Output_location_W,1)
                    self.delet_copy(self.s2,self.sub_dest)

                    print "created"
        '''

















#op().get_des_location(Constans.W_dest_BHO)

#op().test()

