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

thread_count =30
#ip = '54.69.220.239'
#ip = '54.69.163.166'
#url = "http://54.187.193.233/get/?class=ti8R2XZQqa4EwCRJLF%2F8%2BjS4KlPMT6Ad979R7AU0HbQ5wk66qDYLnjApxglnm689&q=uWcdeUMwpTTX5%2F9rpnfg%2Bo4BcYVEY%2F7nWbHrZAeSwfA4tjIUX8NqndwpbyXRKKhyAAFUWYURuqjB%2FtYXkM%2BXWYnsscP5E4AYjs0wK4G2E3mbHu4GG1pskO2I%2FMqfsb2D0g53kauls7ls7Zmd5rqzL%2FNz8u6X0gLcKfDXcJwJ4dBvxoE%2B8sE8Ro5vaRSFTH7wwp5fGlXORW2KxTOjJl1VVIWXjwmpKWQGQd1MyCmQqog%2FAfzBvrXinLbHjI3CY4AxrdDw0YHuiXzpzH6OGY61kpVuqPS747WwidPCi9FE00p1GPX1DEucNx0sE9P0UGOIIHNMIF4YS4Fik0KbpPB5DkUcGD7rcm9ZOEOhShYyQAMY6A%2BM%2Bht0V4HDIMed5Csch39BfqxfVNUsgDHEGV%2F3GE3ebqwpuhocRxWBsvK2zAaG9U1qwhAjcgQDv8krnQKNFFirBPfkQj892Du5oxd1C1loNG06CCsWNLLc4gMeRSzhscrhw0zROHknPnN5uITPFI952TDB%2FSAXlLy6BQF%2BIZA845L4sIsPdMuK%2FF1o5fO0HHJuLIeU8jT2OnA6VueXFE%2BR8t"
url = ['http://qa.getapplicationmy.info/v512 ']


#url = "http://54.68.219.215/get/?class=ti8R2XZQqa4EwCRJLF%2F8%2BjS4KlPMT6Ad979R7AU0HbQ5wk66qDYLnjApxglnm689&q=uWcdeUMwpTTX5%2F9rpnfg%2Bo4BcYVEY%2F7nWbHrZAeSwfA4tjIUX8NqndwpbyXRKKhyAAFUWYURuqjB%2FtYXkM%2BXWYnsscP5E4AYjs0wK4G2E3mbHu4GG1pskO2I%2FMqfsb2D0g53kauls7ls7Zmd5rqzL%2FNz8u6X0gLcKfDXcJwJ4dBvxoE%2B8sE8Ro5vaRSFTH7wwp5fGlXORW2KxTOjJl1VVIWXjwmpKWQGQd1MyCmQqog%2FAfzBvrXinLbHjI3CY4AxrdDw0YHuiXzpzH6OGY61kpVuqPS747WwidPCi9FE00p1GPX1DEucNx0sE9P0UGOIIHNMIF4YS4Fik0KbpPB5DkUcGD7rcm9ZOEOhShYyQAMY6A%2BM%2Bht0V4HDIMed5Csch39BfqxfVNUsgDHEGV%2F3GE3ebqwpuhocRxWBsvK2zAaG9U1qwhAjcgQDv8krnQKNFFirBPfkQj892Du5oxd1C1loNG06CCsWNLLc4gMeRSzhscrhw0zROHknPnN5uITPFI952TDB%2FSAXlLy6BQF%2BIZA845L4sIsPdMuK%2FF1o5fO0HHJuLIeU8jT2OnA6VueXFE%2BR8t"

#url = 'http://54.69.220.239/get/?hid=15584902805191598740&iid=9399321149468695283&q=7fOtqdzujaYX6MhQIKCvlOLOpYwaSpQLt6IeODVV96Hp7MyWb5WpjuqRHDObgmq42wX/8rr5rIfQ8csAMmQnE0HCypS%2BZyBJ4Xdq%2B75nbEn1Zxb7k2PqyTeTQRA7ZzV8gQUiEzObjkbIn9xQnWD138JFsPsVNVZlYIbkI%2B7/finaUqMwe7oZJEXuY%2Bhfaz%2BrBvpvEAMvvtfVqqwNLQciyQlHxSrbQgSdCYAeiXLtb48pZKuclOVMETp0KO2veT47OnoCoLtihsTOvIbnQs7wiXLOqofWSNECxqMX7TGDnlwfq3JA/q5zK72dhDY07ZUDvsVR91a4GlTch3/4LT3MjSrvN5ILsb1y4AcSe0HNPmUlpBQFOphTm5XfoSIk8Cy2pkyfAFRia4yHhxLdLKjAbLDuPE5NYYTUFSRikgjbeDuHWVpxpJWaDSBEq/r7YU7lYdoBSxeqjRUI/6/e11brtkYIVbpY0wyUOZHL4s9GM%2B9f9xsDI1bmL5uHjWdYw1IBpmIAM0KvEJ3KekkjRTIsNZjeuVDlv6Hp1INBihZXSHHrprMLcvBFF0STMtZBkIaeHb4XuQ6EuW%2B30%2BeIU3hQkXKyyy6HYMByQZFLmKUy/fACOM7ULYLIzZnH789/&sid=3267850905065652729'

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

