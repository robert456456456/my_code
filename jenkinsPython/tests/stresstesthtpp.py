import threading
import time
import urllib2
import datetime
from sets import Set
import random
from copy import deepcopy
import urlparse
#import base64x
import json

thread_count =20
url = ['http://ec2-54-69-94-190.us-west-2.compute.amazonaws.com?e=wxd&dd=20&ams=1&emnum=50&jc=1&fc=1&s_id=15&register_date=120707000000&zyccode=us ']
delay = 60
exitFlag = 0
results = {}







for link in url:

    results[link] = {}
    results[link]['responses'] = 0
    results[link]['requests'] = 0
    results[link]['fails'] = 0
    results[link]['total_requests'] = []
    results[link]['total_responses'] = []
    results[link]['total_fails'] = []
#times = []
#print urllib2.urlopen(url).read()
'''
array = ["1", "2", "1" ,"2" ,"3" ,"5", "1", "2", "4"]
crap = set(array)
for e in crap:
    print e
'''


class Requests (threading.Thread):
    def __init__(self, threadID, name, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = url

    def run(self):
        request(self.url)


def request(link):

    try:
        xx = urllib2.urlopen(link, timeout=600)
        x = xx.read()
        results[link]['requests'] += 1
        if not (x == "" or x.isspace()):

            results[link]['responses'] += 1

    except:

        results[link]['fails'] += 1


class CountClear (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print "Starting " + self.name
        count_clear()
        print "Exiting " + self.name


def count_clear():
    while True:
        print
        time.sleep(delay)
        print datetime.datetime.now()

        tmp_dict = deepcopy(results)

        for address in tmp_dict:
            a = results[address]['requests']
            b = results[address]['responses']
            c = results[address]['fails']
            results[address]['total_requests'].append(a)
            results[address]['total_responses'].append(b)
            results[address]['total_fails'].append(c)
            results[address]['requests'] -= a
            results[address]['responses'] -= b
            results[address]['fails'] -= c

        tmp_dict = deepcopy(results)

        p_counter = 0
        for x in tmp_dict:

            publisher = ''
            query = urlparse.parse_qs(x)
            for y in query:
                if y in ['q', 'data']:
                    '''
                    a = query[y][0]
                    a = urllib2.unquote(a)
                    a = base64x.decode(a)
                    a = json.loads(a)
                    try:
                        publisher = a['defender_activity']['publisher_id']
                    except:
                        try:
                            publisher = a['agent_activity']['publisher_id']
                        except:
                            pass
                    '''
                    pass
            if publisher == '':
                publisher = p_counter
                p_counter += 1

            print publisher
            print 'requests:'
            print tmp_dict[x]['total_requests']
            print 'responses:'
            print tmp_dict[x]['total_responses']
            print 'fails:'
            print tmp_dict[x]['total_fails']
            print
            print

        print datetime.datetime.now()



count =0
while count < 2:
    thread1 = CountClear(1, "Clearing")
    thread1.start()
    counter = 1
    count = count + 1
    print count
    while True:

        if count != 2:
            #print count
            randint = random.randint(0, len(url) - 1)
            #print randint
            if threading.activeCount() < thread_count:
                Requests(counter, "Requests", url[randint]).start()
                counter += 1
        else:
            print "end test"


    #print threading.activeCount()

