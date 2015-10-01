import shutil
import urllib2
import subprocess
import os
import time
import Constans


class Builder_checker:
    def download(self, host, param, path ):

            url = 'http://'+host+"/"+param
            u = urllib2.urlopen(url)
            meta = u.info()
            name = str(meta.getheaders("Content-Disposition"))
            fname = name[24:-3]
            if not os.path.exists(os.getcwd() + "\\" + path):
                os.makedirs(os.getcwd() + "\\" + path)
            f = open(os.getcwd() + "\\" + path + "\\" + fname, 'wb')
            file_size = int(meta.getheaders("Content-Length")[0])
            print "self.downloading: %s Bytes: %s" % (fname, file_size)
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
                #print status,

            f.close()
            #print fname
            b = fname[0:len(fname)-4]
            #print b
            subprocess.Popen([os.getcwd()+'\craparc.exe','-x',os.getcwd()+"\\"+path +"\\"+fname,os.getcwd()+"\\"+path +"\\"+b], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
            time.sleep(10)
            print os.getcwd()+"\\"+path+"\\"+b
            shutil.rmtree(os.getcwd()+"\\"+path+"\\")
            return fname


    def QA(self):
        count_chrome_silicon_32_QA = Constans.Count_num_start
        count_chrome_silicon_64_QA = Constans.Count_num_start
        count_ff_silicon_qa = Constans.Count_num_start
        count_bijo_test_QA=Constans.Count_num_start
        count_BHO_test_QA=Constans.Count_num_start
        count_QA_live_link=Constans.Count_num_start
        print "chrome silicon 32 QA"
        while count_chrome_silicon_32_QA != Constans.Count_num_end:
            self.download(Constans.QA_Builder_url,Constans.Param_Chrome_silicon_32,Constans.PATH)
            count_chrome_silicon_32_QA = count_chrome_silicon_32_QA+1
        print "chrome silicon 64 QA"
        while count_chrome_silicon_64_QA != Constans.Count_num_end:
            self.download(Constans.QA_Builder_url,Constans.Param_Chrome_silicon_32,Constans.PATH)
            count_chrome_silicon_64_QA  = count_chrome_silicon_64_QA+1
        print "ff silicon qa"
        while count_ff_silicon_qa != Constans.Count_num_end:
            self.download(Constans.QA_Builder_url,Constans.Param_FF_silicon,Constans.PATH)
            count_ff_silicon_qa  = count_ff_silicon_qa+1
        print "bijo test QA"
        while count_bijo_test_QA != Constans.Count_num_end:
            self.download(Constans.QA_Builder_url,Constans.Param_BIHO,Constans.PATH)
            count_bijo_test_QA  = count_bijo_test_QA+1
        print "BHO test QA"
        while count_BHO_test_QA != Constans.Count_num_end:
            self.download(Constans.QA_Builder_url,Constans.Param_BIHO,Constans.PATH)
            count_BHO_test_QA  = count_BHO_test_QA+1
        print "QA live link"
        while count_QA_live_link != Constans.Count_num_end:
            self.download(Constans.QA_Builder_url,Constans.Param_Live,Constans.PATH)
            count_QA_live_link  = count_QA_live_link+1
        return "end test QA  Builder"

    def bijo_BHO_p(self):
        print "pro BHO/bijo 32 test pro"
        print Constans.Main_Builder_url+Constans.Brand_Main
        self.download(Constans.Main_Builder_url,Constans.Param_BIJO,Constans.PATH)
        print Constans.Fallback_1_Builder_url+Constans.Brand_Fallback_1
        self.download(Constans.Fallback_1_Builder_url,Constans.Param_BIJO,Constans.PATH)
        print Constans.Fallback_2_Builder_url+Constans.Brand_Fallback_2
        self.download(Constans.Fallback_2_Builder_url,Constans.Param_BIJO,Constans.PATH)
        print Constans.Primary_Update_Builder_url+Constans.Brand_Primary_Update
        self.download(Constans.Primary_Update_Builder_url,Constans.Param_BIJO,Constans.PATH)
        print Constans.Panda_1_Builder_url+Constans.Brand_Panda_1
        self.download(Constans.Panda_1_Builder_url,Constans.Param_BIJO,Constans.PATH)
        print Constans.Panda_2_Builder_url+Constans.Brand_Panda_2
        self.download(Constans.Panda_2_Builder_url,Constans.Param_BIJO,Constans.PATH)
        print Constans.Media_Buying_Builder_url+Constans.Brand_Media_Buying
        self.download(Constans.Media_Buying_Builder_url,Constans.Param_BIJO,Constans.PATH)
        print Constans.Teddy_Builder_url+Constans.Brand_Teddy
        self.download(Constans.Teddy_Builder_url,Constans.Param_BIJO,Constans.PATH)
        print Constans.Zet_Builder_url+Constans.Brand_Zet
        self.download(Constans.Zet_Builder_url,Constans.Param_BIJO,Constans.PATH)

        print "pro BHO 32 test pro"
        print Constans.Main_Builder_url+Constans.Brand_Main
        self.download(Constans.Main_Builder_url,Constans.Param_BIHO,Constans.Main_Builder_url)
        print Constans.Fallback_1_Builder_url+Constans.Brand_Fallback_1
        self.download(Constans.Fallback_1_Builder_url,Constans.Param_BIHO,Constans.Main_Builder_url)
        print Constans.Fallback_2_Builder_url+Constans.Brand_Fallback_2
        self.download(Constans.Fallback_2_Builder_url,Constans.Param_BIHO,Constans.Main_Builder_url)
        print Constans.Primary_Update_Builder_url+Constans.Brand_Primary_Update
        self.download(Constans.Primary_Update_Builder_url,Constans.Param_BIHO,Constans.Main_Builder_url)
        print Constans.Panda_1_Builder_url+Constans.Brand_Panda_1
        self.download(Constans.Panda_1_Builder_url,Constans.Param_BIHO,Constans.Main_Builder_url)
        print Constans.Panda_2_Builder_url+Constans.Brand_Panda_2
        self.download(Constans.Panda_2_Builder_url,Constans.Param_BIHO,Constans.Main_Builder_url)
        print Constans.Media_Buying_Builder_url+Constans.Brand_Media_Buying
        self.download(Constans.Media_Buying_Builder_url,Constans.Param_BIHO,Constans.Main_Builder_url)
        print Constans.Teddy_Builder_url+Constans.Brand_Teddy
        self.download(Constans.Teddy_Builder_url,Constans.Param_BIHO,Constans.Main_Builder_url)
        print Constans.Zet_Builder_url+Constans.Brand_Zet
        self.download(Constans.Zet_Builder_url,Constans.Param_BIHO,Constans.Main_Builder_url)
        return " end test "


    def chrome_sillicon_64(self):
        print "new silicon 64 test pro start test"
        print Constans.Main_Builder_url+Constans.Brand_Main
        self.download(Constans.Main_Builder_url,Constans.Param_Chrome_silicon_64,Constans.Main_Builder_url)
        print Constans.Fallback_1_Builder_url+Constans.Brand_Fallback_1
        self.download(Constans.Fallback_1_Builder_url,Constans.Param_Chrome_silicon_64,Constans.Main_Builder_url)
        print Constans.Fallback_2_Builder_url+Constans.Brand_Fallback_2
        self.download(Constans.Fallback_2_Builder_url,Constans.Param_Chrome_silicon_64,Constans.Main_Builder_url)
        print Constans.Primary_Update_Builder_url+Constans.Brand_Primary_Update
        self.download(Constans.Primary_Update_Builder_url,Constans.Param_Chrome_silicon_64,Constans.Main_Builder_url)
        print Constans.Panda_1_Builder_url+Constans.Brand_Panda_1
        self.download(Constans.Panda_1_Builder_url,Constans.Param_Chrome_silicon_64,Constans.Main_Builder_url)
        print Constans.Panda_2_Builder_url+Constans.Brand_Panda_2
        self.download(Constans.Panda_2_Builder_url,Constans.Param_Chrome_silicon_64,Constans.Main_Builder_url)
        print Constans.Media_Buying_Builder_url+Constans.Brand_Media_Buying
        self.download(Constans.Media_Buying_Builder_url,Constans.Param_Chrome_silicon_64,Constans.Main_Builder_url)
        print Constans.Teddy_Builder_url+Constans.Brand_Teddy
        self.download(Constans.Teddy_Builder_url,Constans.Param_Chrome_silicon_64,Constans.Main_Builder_url)
        print Constans.Zet_Builder_url+Constans.Brand_Zet
        self.download(Constans.Zet_Builder_url,Constans.Param_Chrome_silicon_64,Constans.Main_Builder_url)
        return "end test chrome silicon 64"




    def chrome_silicon_32(self):
        print "new silicon 32 test pro start test"
        print Constans.Main_Builder_url+Constans.Brand_Main
        self.download(Constans.Main_Builder_url,Constans.Param_Chrome_silicon_32,Constans.Main_Builder_url)
        print Constans.Fallback_1_Builder_url+Constans.Brand_Fallback_1
        self.download(Constans.Fallback_1_Builder_url,Constans.Param_Chrome_silicon_32,Constans.Main_Builder_url)
        print Constans.Fallback_2_Builder_url+Constans.Brand_Fallback_2
        self.download(Constans.Fallback_2_Builder_url,Constans.Param_Chrome_silicon_32,Constans.Main_Builder_url)
        print Constans.Primary_Update_Builder_url+Constans.Brand_Primary_Update
        self.download(Constans.Primary_Update_Builder_url,Constans.Param_Chrome_silicon_32,Constans.Main_Builder_url)
        print Constans.Panda_1_Builder_url+Constans.Brand_Panda_1
        self.download(Constans.Panda_1_Builder_url,Constans.Param_Chrome_silicon_32,Constans.Main_Builder_url)
        print Constans.Panda_2_Builder_url+Constans.Brand_Panda_2
        self.download(Constans.Panda_2_Builder_url,Constans.Param_Chrome_silicon_32,Constans.Main_Builder_url)
        print Constans.Media_Buying_Builder_url+Constans.Brand_Media_Buying
        self.download(Constans.Media_Buying_Builder_url,Constans.Param_Chrome_silicon_32,Constans.Main_Builder_url)
        print Constans.Teddy_Builder_url+Constans.Brand_Teddy
        self.download(Constans.Teddy_Builder_url,Constans.Param_Chrome_silicon_32,Constans.Main_Builder_url)
        print Constans.Zet_Builder_url+Constans.Brand_Zet
        self.download(Constans.Zet_Builder_url,Constans.Param_Chrome_silicon_32,Constans.Main_Builder_url)
        return "end test new silicon 32 test pro "


    def ff_silicon_pro(self):
        print "new silicon ff 32/64 test pro"
        print Constans.Main_Builder_url+Constans.Brand_Main
        self.download(Constans.Main_Builder_url,Constans.Param_FF_silicon,Constans.Main_Builder_url)
        print Constans.Fallback_1_Builder_url+Constans.Brand_Fallback_1
        self.download(Constans.Fallback_1_Builder_url,Constans.Param_FF_silicon,Constans.Main_Builder_url)
        print Constans.Fallback_2_Builder_url+Constans.Brand_Fallback_2
        self.download(Constans.Fallback_2_Builder_url,Constans.Param_FF_silicon,Constans.Main_Builder_url)
        print Constans.Primary_Update_Builder_url+Constans.Brand_Primary_Update
        self.download(Constans.Primary_Update_Builder_url,Constans.Param_FF_silicon,Constans.Main_Builder_url)
        print Constans.Panda_1_Builder_url+Constans.Brand_Panda_1
        self.download(Constans.Panda_1_Builder_url,Constans.Param_FF_silicon,Constans.Main_Builder_url)
        print Constans.Panda_2_Builder_url+Constans.Brand_Panda_2
        self.download(Constans.Panda_2_Builder_url,Constans.Param_FF_silicon,Constans.Main_Builder_url)
        print Constans.Media_Buying_Builder_url+Constans.Brand_Media_Buying
        self.download(Constans.Media_Buying_Builder_url,Constans.Param_FF_silicon,Constans.Main_Builder_url)
        print Constans.Teddy_Builder_url+Constans.Brand_Teddy
        self.download(Constans.Teddy_Builder_url,Constans.Param_FF_silicon,Constans.Main_Builder_url)
        print Constans.Zet_Builder_url+Constans.Brand_Zet
        self.download(Constans.Zet_Builder_url,Constans.Param_FF_silicon,Constans.Main_Builder_url)
        return "end test "

