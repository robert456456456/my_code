__author__ = 'user'

import os
import datetime
import time
import shutil

target = "C:\\.media\\websites\\exe"


def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]


print get_immediate_subdirectories(target)
bob = []
bob = get_immediate_subdirectories(target)

'''
#print bob[7]
for index, value in enumerate(bob):
    #index += 7
    print value
    print target+"\\"+value
    path=target+"\\"+value
    seconds = os.path.getmtime(path)
    print time.strftime('%Y-%m-%d %H:%M', time.localtime(seconds))
'''


def mediy_copy(c1, c2, lp, source, dest):
    source1 = source + c1 + ".exe"
    dest1 = dest + "dl" + c2 + ".costmin.info\\tmps.exe"
    while lp:
        shutil.copy2(source1,dest1)
    else:
            break
    return

    ''''
def get_date(path1):
    for x in range(len(path1)):
        a = x + 7
        try:
            # print target + bob[a]
            #print target+"\\"+bob[a]
            path = target + "\\" + path1[a] + "\\" + "tmps.exe"
            path1 = target + "\\" + path1[a] + "\\" + "tmps.g23"
            seconds = os.path.getmtime(path)
            seconds1 = os.path.getmtime(path1)

            print time.strftime('%Y-%m-%d %H:%M', time.localtime(seconds))
            print time.strftime('%Y-%m-%d %H:%M', time.localtime(seconds1))
            D_T = time.strftime('%Y-%m-%d %H:%M', time.localtime(seconds)) + time.strftime('%Y-%m-%d %H:%M',
                                                                                           time.localtime(seconds1))
        except:
            break
        return (D_T)


get_date(bob)
'''''''''''''''
    sor = "C:\\dev\\shite\\recompiled"
    des = "C:\\.media\\websites\\exe"
    lo = 5000
    co1 = 107
    co2 = 5102

    mediy_copy(co1, co2, lo, sor, des)