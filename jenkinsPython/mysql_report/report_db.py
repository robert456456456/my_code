import sys
import pymongo
import MySQLdb as qdb
import urllib
import urllib2
import random
import datetime
import time
import string
import base64x

def brows_ver():
    browser_id = 1
    range = random.randrange(0, 6,1)
    i=0
    while i < range:
        browser_id = browser_id << 1
        i+=1
    return str(browser_id)

def ser_pack():
    range = random.randrange(0, 6,1)
    return str(range)

def bool_int():
    range = random.randrange(0, 2,1)
    return str(range)

def time_id():
    dt = datetime.datetime.now()
    all=string.maketrans('','')
    nodigs=all.translate(all, string.digits)
    dt = str(dt).translate(all, nodigs)
    return str(dt[0:19])

def send_rep(data):
    url = "http://r1.qa.getapplicationmy.info/?report_version=5&"
    header = {'Host': 'r1.qa.getapplicationmy.info',
          'Content-Length': len(data),
          'Connection': 'close',
          'User-Agent':'TixDll',
          'Accept-Encoding': '',
          'Pragma': 'no-cache',
          'Accept': '*/*'}

    print "Sending report..."
    req = urllib2.Request(url, data, header)
    response = urllib2.urlopen(req)
    serv_response = response.read()
    print serv_response
    if serv_response != '{}':
        sys.exit("Sending report Failed!!!")
    return serv_response

def mysql_rep_check(rep_try):
    try:
        print "Waiting 180 sec..."
        time.sleep(180)

        print "Sending MongoDB Request..."
        from pymongo import MongoClient
        client = MongoClient('ec2-54-185-32-28.us-west-2.compute.amazonaws.com', 27017)
        db = client['qa']
        query = db.bot.find({"report_id.installer_id" : timer_id}).count()
        if query != 1:
            sys.exit("Mongo DB report faild!!!")
        print "MongoDB report Succeeded..."

        con = qdb.connect(host="qabox.webpick.net", user="anton", passwd="aq1sw2de3fr4", db="installer_analytics_server")
        print "MySql connect to qabox.webpick.net..."
        cur = con.cursor()
        print "Waiting 2min for MySql report arriving..."
        query = "SELECT Count(today_installers_started.installer_id) FROM `today_installers_started` WHERE today_installers_started.installer_id = "+ '"' + str(timer_id) + '"'
        print "Sending MySql Request..."
        print query
        cur.execute(query)
        for row in cur:
            print "MySql response: " + str(row[0])
            if str(row[0]) != "1" and rep_try < 5:
                print "MySql Request " + str(rep_try)+ " faild.!."
                if rep_try > 3:
                    sys.exit("MYSQL report faild!!!")
                return mysql_rep_check(rep_try + 1)

        query = "SELECT * FROM `today_installers_started` WHERE today_installers_started.installer_id = "+ '"' + str(timer_id) + '"'
        print "Sending MySql Request 2..."
        print query
        cur.execute(query)
        for row in cur:
            if row[0] == 0:
                print str(row[0]) + " \r\n"
                sys.exit("Report ID error!!!")
            if str(row[1]) != timer_id:
                print str(row[1]) + " \r\n"
                sys.exit("Installer ID error!!!")
            if str(row[2]) != timer_id:
                print str(row[2]) + " Expect "+ timer_id +" \r\n"
                sys.exit("Session ID error!!!")
            if row[3] != 1234567890987654321:
                print str(row[3]) + " Expect 1234567890987654321 \r\n"
                sys.exit("Download ID error!!!")
            if str(row[4]) != timer_id:
                print str(row[4]) + " Expect "+ timer_id +" \r\n"
                sys.exit("Hardware ID error!!!")
            if row[5] != 0:
                print str(row[5]) + " Expect 0 \r\n"
                sys.exit("External ID error!!!")
            if row[6] != 9607:
                print str(row[6]) + " Expect 9607 \r\n"
                sys.exit("Publisher ID error!!!")
            if row[7] != 0:
                print str(row[7]) + " Expect 0 \r\n"
                sys.exit("Suurce ID error!!!")
            if row[8] != 0:
                print str(row[8]) + " Expect 0 \r\n"
                sys.exit("Page ID error!!!")
            if row[9] == 0:
                print str(row[9]) + " Expect not 0 \r\n"
                sys.exit("Affiliate ID error!!!")
            if row[10] == 0:
                print str(row[10]) + " Expect not 0 \r\n"
                sys.exit("IP error!!!")
            if row[11] != "IL":
                print str(row[11]) + " Expect IL \r\n"
                sys.exit("Countru code error!!!")
            if row[12] != "EN":
                print str(row[12]) + " Expect EN \r\n"
                sys.exit("Lang error!!!")
            if row[13] == 0:
                print str(row[13]) + " Expect not 0 \r\n"
                sys.exit("Report Time error!!!")
            if row[14] != 607:
                print str(row[14]) + " Expect 607 \r\n"
                sys.exit("OS ID error!!!")
            if str(row[15]) != serice_pack:
                print str(row[15]) + " Expect "+ serice_pack +" \r\n"
                sys.exit("Service pack error!!!")
            if (bool(row[16]) ^(int(bool_integer))):
                print str(row[16]) + " Expect "+ str(bool_integer) +" \r\n"
                sys.exit("x64 error!!!")
            if bool(row[17]) != True:
                print str(row[17]) + " Expect 1 \r\n"
                sys.exit("Is Admin error!!!")
            if str(row[18]) != brows_version:
                print str(row[18]) + " Expect "+ brows_version +" \r\n"
                sys.exit("Browser ID error!!!")
            if row[19] != 1234567890987654321:
                print str(row[18]) + " Expect 1234567890987654321 \r\n"
                sys.exit("Browser Version ID error!!!")
            if row[20] != 1234567890987654321:
                print str(row[20]) + " Expect 1234567890987654321 \r\n"
                sys.exit("Domain ID error!!!")
            if row[21] != 0:
                print str(row[21]) + " Expect 0 \r\n"
                sys.exit("Refer domain ID error!!!")
            if row[22] != 1234567890987654321:
                print str(row[22]) + " Expect 1234567890987654321 \r\n"
                sys.exit("Query string ID error!!!")
            if row[23] != 1234567890987654321:
                print str(row[23]) + " Expect 1234567890987654321 \r\n"
                sys.exit("User Agent ID error!!!")
            if row[24] != 6007:
                print str(row[24]) + " Expect 6007 \r\n"
                sys.exit("Platform version ID error!!!")
            if row[25] != 1000001:
                print str(row[25]) + " Expect 1000001 \r\n"
                sys.exit("Version error!!!")
            if row[26] != 1234567890987654321:
                print str(row[26]) + " Expect 1234567890987654321 \r\n"
                sys.exit("User ID error!!!")
            if row[27] != 1033:
                print str(row[27]) + " Expect 1033 \r\n"
                sys.exit("User lang ID error!!!")
            if row[28] != 0:
                print str(row[28]) + " Expect not 0 \r\n"
                sys.exit("Antivirus ID error!!!")
            if row[29] != 607:
                print str(row[29]) + " Expect 607 \r\n"
                sys.exit("screen x error!!!")
            if row[30] != 607:
                print str(row[30]) + " Expect 607 \r\n"
                sys.exit("screen y error!!!")
            if row[31] == 0:
                print str(row[31]) + " Expect not 0 \r\n"
                sys.exit("Build Time ID error!!!")
            if str(row[32]) != str(bool_integer):
                print str(row[32]) + " Expect "+ str(bool_integer) +" \r\n"
                sys.exit("Is signet error!!!" + str(row[32]))

    except qdb.Error as e:
        print(con.error())
    print "MySql report Succeeded..."
    return


brows_version = brows_ver()
serice_pack = ser_pack()
bool_integer = bool_int()
timer_id = time_id()
timen = datetime.datetime.now()
daten = timen.strftime('%y/%m/%d')
timen = timen.strftime('%H:%M:%S')

data1 = '{' \
        '"installer_products": [],"installer_software": [{"n": "undefined",	"v": "1.0.0.0001"}],' \
        '"installer_started":{"installer_id":"'+timer_id+'",' \
        '"session_id":"'+timer_id+'", ' \
        '"hardware_id":"'+timer_id+'", ' \
        '"external_id":"0", "version":"75", ' \
        '"platform_version":"6007", ' \
        '"publisher_id":"9607", ' \
        '"source_id":"0", ' \
        '"page_id":"0", ' \
        '"download_id":"1234567890987654321", ' \
        '"affiliate_id":"botest", ' \
        '"user_id":"1234567890987654321", ' \
        '"is_admin":"1", ' \
        '"user_lang_id":"1033", ' \
        '"lang":"EN",' \
        '"os_id":"607", ' \
        '"x64":"'+bool_integer+'", ' \
        '"service_pack":"'+serice_pack+'", ' \
        '"browser_id":"'+brows_version+'", ' \
        '"browser_version_id":"1234567890987654321", ' \
        '"screen_x":"607", ' \
        '"screen_y":"607", ' \
        '"domain_id":"1234567890987654321", ' \
        '"referer_domain_id":"",' \
        '"query_string_id":"1234567890987654321", ' \
        '"user_agent_id":"1234567890987654321", ' \
        '"antivirus_info":"", ' \
        '"build_time":"'+timer_id[0:14]+'", ' \
        '"is_signed":"'+bool_integer+'", ' \
        '"signature_name":"otobot",' \
        '"accepts_counter": 0,' \
        '"declines_counter": 0,' \
        '"screens_counter": 0,' \
        '"steps_counter": 0,' \
        '"total_duration": "21",' \
        '"version": "1000001"' \
        '}}'


info = '[{"n":"Bitvise SSH Server 6.04 (remove only)"},' \
       '{"n":"Fiddler","v":"2.4.8.0"},{"n":"Notepad++","v":"5.9.4"},' \
       '{"n":"WinPcap 4.1.3","v":"4.1.0.2980"},{"n":"Wireshark 1.11.0 (64-bit)","v":"1.11.0"},' \
       '{"n":"Microsoft Visual C++ 2008 Redistributable - x86 9.0.30729.4148","v":"9.0.30729.4148"},' \
       '{"n":"Microsoft Visual C++ 2010  x64 Redistributable - 10.0.40219","v":"10.0.40219"},' \
       '{"n":"Microsoft Visual C++ 2008 Redistributable - x64 9.0.30729.4148","v":"9.0.30729.4148"},' \
       '{"n":"VMware Tools","v":"9.4.5.1598834"}]'

sinfo = 'UN:Fiddler|UN:Wireshark 1.11.0 (64-bit)|UN:VMware Tools|MAC:00-50-56-ab-21-52|WIN:Fiddler Web Debugger|EXE:Fiddler.exe'

report = '{	"collection_name": "bot","db_name": "qa","environment": {"CertDlls": {"x64": null,"x64_x86": null,"x86": null},"DetectAV": null,' \
         '"DetectIP": ["Fiddler",	"WinPcap 4.1.3","Wireshark 1.11.0 (32-bit)"	],"IsVM": '+bool_integer+',"UnknownDlls": ' \
         '{"18": "C:\\\\Windows\\\\WinSxS\\\\x86_microsoft.windows.common-controls_6595b64144ccf1df_6.0.7601.17514_none_41e6975e2bd6f2b2"}},' \
         '"installer_products": {},"installer_session": {"exit_code": 2147483658,"exit_reason": "I_still_active","installer_state": ' \
         '{"AcceptCounter": 0,"AffiliateID": "otobot","AppDataFolder": "C:\\\\Users\\\\user\\\\AppData\\\\Local","BrowserID": "'+brows_version+'",' \
         '"BrowserVersionID": "1234567890987654321","CommonAppDataFolder": "C:\\\\ProgramData",' \
         '"ConfigQuery": "installer_id='+timer_id+'&publisher_id=607&source_id=0&page_id=0&affiliate_id=otobot&country_code=IL&locale=EN&browser_id='+brows_version+'&download_id=1234567890987654321&external_id=0&installer_type=IX_2013",' \
         '"CountryCode": "IL","DeclineCounter": 0,"DesktopFolder": "C:\\\\Users\\\\user\\\\Desktop","DomainID": "1234567890987654321",' \
         '"DownloadID": "1234567890987654321","ExternalID": "0",	"FallbackStepID": "1,2,3","HardwareID": "'+timer_id+'",' \
         '"IX_DataFolder": "C:\\\\Users\\\\user\\\\AppData\\\\Local\\\\Temp\\\\5d1e5955","IX_ExeFolder": "C:\\\\Users\\\\user\\\\AppData\\\\Local\\\\Temp\\\\5d1e5955",	' \
         '"IX_ExePath": "C:\\\\Users\\\\user\\\\AppData\\\\Local\\\\Temp\\\\5d1e5955\\\\preloader.exe",	"IX_LogFile": "installerlog.txt",' \
         '"IX_Mode": "release","IX_StateFile": "C:\\\\Users\\\\user\\\\AppData\\\\Local\\\\Temp\\\\5d1e5955\\\\installer\\\\step0.ini",' \
         '"InstallDate": "'+ timer_id[0:8] +'","InstallerDate": "'+ daten +'","InstallerID": "'+timer_id+'",	"InstallerMode": "",' \
         '"InstallerTime": "'+timen+'","Language": "EN","PageID": "0",	"ProfileFolder": "C:\\\\Users\\\\user",	"ProgramFiles64Folder": "",	' \
         '"ProgramFilesFolder": "C:\\\\Program Files",	"ProgramFilesXFolder": "C:\\\\Program Files",	"PublisherID": "607",' \
         '"QueryString": "affiliate_id=boobo&installer_type=IX_2013&IX_LogFile=installerlog.txt&preloader_version=1&installer_version=1&DB_name=qa&collection_name=an&im=LOG&filesize=&product_download_url=%3CServerUrl%3E%2Faddons%2Ferror.txt&reffer=http%3A%2F%2Fuploading.com%2F&product_file_name=error.txt&layout_id=8&for_html_installer=1&uuid=%252A",' \
         '"QueryStringID": "1234567890987654321","QueryVariable_DB_name": "qa",	"QueryVariable_affiliate_id": "boobo",	' \
         '"QueryVariable_collection_name": "an",	"QueryVariable_filesize": "","QueryVariable_for_html_installer": "1",' \
         '"QueryVariable_im": "LOG",	"QueryVariable_installer_type": "IX_2013",	"QueryVariable_installer_version": "1",	' \
         '"QueryVariable_layout_id": "8",	"QueryVariable_preloader_version": "1",	"QueryVariable_product_download_url": "<ServerUrl>/addons/error.txt",' \
         '"QueryVariable_product_file_name": "error.txt","QueryVariable_reffer": "http://uploading.com/","QueryVariable_uuid": "%2A","RefererDomainID": "",' \
         '"RunOnceID": "","ScreenCounter": 0,"ServerCfgUrl": "http://c1.qa.getapplicationmy.info","ServerCfgUrl1": "http://c2.qa.getapplicationmy.info",' \
         '"ServerName": "Vertx1","ServerReportUrl": "http://r1.qa.getapplicationmy.info","ServerReportUrl1": "http://r2.qa.getapplicationmy.info","ServerScreenUrl": "http://s1.qa.getapplicationmy.info",' \
         '"ServerScreenUrl1": "http://s2.qa.getapplicationmy.info",	"ServerUrl": "http://i1.qa.getapplicationmy.info",' \
         '"ServerUrl1": "http://i2.qa.getapplicationmy.info","SessionID": "'+timer_id+'","ShowInTaskbar": "'+bool_integer+'",' \
         '"SingleInstanceID": "","SourceID": "0","SystemFolder": "C:\\\\Windows\\\\System32","TempFolder": "C:\\\\Users\\\\user\\\\AppData\\\\Local\\\\Temp",' \
         '"UserAgentID": "1234567890987654321",	"VersionCLR": 3500,	"VersionNT": 601,"WindowsFolder": "C:\\\\Windows","parameter0": "C:\\\\Users\\\\user\\\\AppData\\\\Local\\\\Temp/5d1e5955/preloader.exe",' \
         '"parameter1": "ProfileFileName=step0.ini"	},"installer_version": {"flags": "R+pecrypt","recompiler": "0",	"version": "1.0.0.0001"	},' \
         '"is_admin": 1,"os": {"arch": "x86","langid": 1033,"major": 6,	"major_minor": 607,	"minor": 1,	"ntdll_build": 7601,"ntdll_major": 6,"ntdll_minor": 1,"runtime": "x86",	"service": '+serice_pack+'},' \
         '"sreen": {"ScreenDigitizer": 0,"ScreenX": 607,"ScreenY": 607,"Tablet": 0	},' \
         '"steps_sequence": [],	"total_duration": "607"},"report_id": {"hardware_id": "'+timer_id+'",	"id": "'+timer_id[0:14]+'",	"installer_id": "'+timer_id+'",' \
         '"reporter": "InstallerEx_2013","reporter_version": "1000001",	"session_id": "'+timer_id+'","type": "installer_started"}}'

finish_rep = '{"installer_products":[{"product_id":"607","step_id":"67","next_step_id":"67","sub_product_id":"67",' \
             '"screen_id":"67",	"screen_counter":"67","channel":"67","user_selection":"253","connection_issues":"67",' \
             '"total_duration":"6007","validate_duration":"607","offer_duration":"607", "download_duration":"607",' \
             '"download_error_code":"607", "install_duration":"607", "file_size":"607", "file_name":"BotoSetapo.exe", ' \
             '"file_crc":"1234567890987654321", "status":"203", "download_url":"http://botoboloto/BotoSetapo.exe", ' \
             '"run_arguments":"botoloto /s", "exit_code":"607"}],"installer_finished":{"installer_id":"'+timer_id+'",' \
             '"session_id":"'+timer_id+'", "version":"607", "total_duration":"60007","steps_counter":"67", ' \
             '"screens_counter":"67", "accepts_counter":"67", "declines_counter":"67"},	"installer_software":[{"n":"Installmate Internet Explorer", ' \
             '"v":"8.0.7600.16385"},{"n":"Installmate Chrome", "v":"35.0.1916.114"},{"n":"Installmate Microsoft .NET", "v":"3051"},' \
             '{"n":"Installmate MSI", "v":"5.0.7600.16385"}]}'


data = "data=" + base64x.encode_any(data1, "UTF-8") + "&info=" + base64x.encode_any(info, "UTF-8") +"&sinfo=" + base64x.encode_any(sinfo, "UTF-8") + "&report=" + base64x.encode_any(report, "UTF-8")+ " \r\n\r\n"
print data
print timer_id

print "Sending universal Started report..."
req = send_rep(data)
print "Sending universal Started report Succeeded..."

data = "data=" + base64x.encode_any(finish_rep, "UTF-8")
print "Sending finish report..."
req = send_rep(data)
print "Sending finish report Succeeded..."

print "Waiting 10 sec..."
time.sleep(20)
print "Sending report pusher..."
req = send_rep("report_pusher=1")
print "Sending report pusher Succeeded..."

mysql_rep_check(0)

sys.exit(0)
