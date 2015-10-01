__author__ = 'Robert Adinihy'

import paramiko
import Constans
import Builder_Constructor
import Installer_Builder_Constructor

class Builder_compiler:


    def costrator_Al(self,brand_co):
        #Main
        b_main = Builder_Constructor.Builder_constructor(Constans.Brand_Main,brand_co)
        b_main.p()
        #Fallback_1
        b_Fallback_1= Builder_Constructor.Builder_constructor(Constans.Brand_Fallback_1,brand_co)
        b_Fallback_1.p()
        #Fallback_2
        b_Fallback_2 = Builder_Constructor.Builder_constructor(Constans.Brand_Fallback_2,brand_co)
        b_Fallback_2.p()
        #panda_1
        b_panda_11 = Builder_Constructor.Builder_constructor(Constans.Brand_Panda_1,brand_co)
        b_panda_11.p()
        #panda_2
        b_panda_22 = Builder_Constructor.Builder_constructor(Constans.Brand_Panda_2,brand_co)
        b_panda_22.p()
        #Teddy
        b_Teddy = Builder_Constructor.Builder_constructor(Constans.Brand_Teddy,brand_co)
        b_Teddy.p()
        #Zet
        b_Zet = Builder_Constructor.Builder_constructor(Constans.Brand_Zet,brand_co)
        b_Zet.p()
        #MD
        b_Media_Buying = Builder_Constructor.Builder_constructor(Constans.Brand_Media_Buying,brand_co)
        b_Media_Buying.p()
        #primery_update
        b_Primary_Update = Builder_Constructor.Builder_constructor(Constans.Brand_Primary_Update,brand_co)
        b_Primary_Update.p()





    def costrator_Al_I(self,brand_co):
        b_installer_1=Installer_Builder_Constructor.Builder_constructor(Constans.I_type1,brand_co)
        b_installer_1.p()


        b_installer_2=Installer_Builder_Constructor.Builder_constructor(Constans.I_type2,brand_co)
        b_installer_2.p()

        b_installer_3=Installer_Builder_Constructor.Builder_constructor(Constans.I_type,brand_co)
        b_installer_3.p()

