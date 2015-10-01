from glob import glob
import re
import MySQLdb

array = glob("/nas/QA/Andrey/report/ROBOT/CrapShitReport/*.*")

'''
def insertToDB(link, publisher, publisher_status, bits, duplicate):
    try:
        conn = MySQLdb.connect(host="dbase.webpick.net", user="media_alert", passwd="aq1sw2de3fr4", db="PingDom")
        x = conn.cursor()
        query = "REPLACE INTO QA_mediabuying (link, publisher_id, alert_status, bits, duplicate) VALUES('" + link + "'," + publisher + ", " + str(int(publisher_status)) + ", " + str(int(bits)) + ", " + str(int(duplicate)) + ')'
        print "Insert : "+query
        x.execute(query)
        conn.commit()
        conn.close()
    except:
        pass
'''

def insertToDB(results):

    conn = MySQLdb.connect(host="dbase.webpick.net", user="media_alert", passwd="aq1sw2de3fr4", db="PingDom")
    a = conn.cursor()
    for x in results:
        link = results[x]['link']
        publisher = results[x]['publisher']
        publisher_status = results[x]['correct publisher']
        bits = results[x]['bits']
        duplicate = results[x]['duplicates']
        query = "REPLACE INTO QA_mediabuying (link, publisher_id, alert_status, bits, duplicate) VALUES('" + link + "'," + publisher + ", " + str(int(publisher_status)) + ", " + str(int(bits)) + ", " + str(int(duplicate)) + ')'
        print "Insert : "+query
        a.execute(query)
        #print 2
        conn.commit()
    conn.close()


def gavno(files_list):
    publishers_array = []
    publisher_dict = {}
    duplicates = {}
    result = {}

    for x in files_list:
        print '---------------------------------------------------------------------------------------'

        bits = False
        publisher = False
        f = open(x, 'rb').read()
        g = open(x, 'rb').readlines()
        '''
        found_publisher = re.search('&PID=(.+?) ', f)
        try:
            found_publisher = found_publisher.group(1)
        except:
            found_publisher = 0
        print found_publisher
        '''
        for line in g:
            if "Location: http://" in line:
                link = line.replace("Location: ", "")
                link = link.replace('\n', "")
                link = link.replace("\r", "")
                print link
                method = re.search('Location: http://(.+?)\.', line)
                subdomain = method.group(1)
                if subdomain[0:2] == "dl":
                    request_type = "dl"
                    short_publisher = subdomain[2::]
                else:
                    request_type = subdomain
                    tmp_line = line.replace("/", " ")
                    crap = [int(s) for s in tmp_line.split() if s.isdigit()]
                    short_publisher = crap[0]
                break

        if 'BITS=11' in f:
            bits = True
        else:
            #print "no bits"
            pass

        if request_type == "dl":
            long_publisher = 5000 + int(short_publisher) - 2
            long_publisher = str(long_publisher)
            if "PID=" + long_publisher in f:
                publisher = True
            else:
                #print "bad publisher"
                long_publisher = "0"

        if request_type == "get":
            long_publisher = 7000 + int(short_publisher)
            long_publisher = str(long_publisher)
            if "PID=" + long_publisher in f:
                publisher = True
            else:
                #print "bad publisher"
                long_publisher = "0"

        if request_type == "app":
            long_publisher = 8000 + int(short_publisher)
            long_publisher = str(long_publisher)
            if "PID=" + long_publisher in f:
                publisher = True
            else:
                long_publisher = "0"




        if long_publisher:
            publisher_dict[link] = long_publisher
        else:
            long_publisher = ""

        if publisher and bits:
            success = True
        else:
            success = False

        #print x
        #print success

        result[link] = {"link": link, "publisher": long_publisher, "correct publisher": publisher, "bits": bits}

    #print publisher_dict

    for x in publisher_dict:
        publishers_array.append(publisher_dict[x])

    for x in publisher_dict:
        counter = 0
        a = publisher_dict[x]
        for aa in publishers_array:
            if a == aa:
                counter += 1
        if counter > 1 and a != "0":
            duplicates[x] = publisher_dict[x]
            result[x]['duplicates'] = True
        else:
            result[x]['duplicates'] = False


    #print duplicates
    #print result
    insertToDB(result)
gavno(array)