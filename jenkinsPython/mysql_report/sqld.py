__author__ = 'User'
from glob import glob
import re
import MySQLdb

def insertToDB():

    conn = MySQLdb.connect(host="dbase.webpick.net", user="media_alert", passwd="aq1sw2de3fr4", db="PingDom")
    a = conn.cursor()
    #query = "REPLACE INTO QA_mediabuying (link, publisher_id, alert_status, bits, duplicate) VALUES('" + link + "'," + publisher + ", " + str(int(publisher_status)) + ", " + str(int(bits)) + ", " + str(int(duplicate)) + ')'
    query = "DELETE FROM QA_mediabuying [WHERE Clause]"
    print "delete : "+query
    a.execute(query)
    #print 2

    conn.commit()
    conn.close()
