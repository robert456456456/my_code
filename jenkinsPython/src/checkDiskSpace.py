#!/usr/bin/python

import os,errno,sys,MySQLdb,datetime,time

def get_mount_point(pathname):
    "Get the mount point of the filesystem containing pathname"
    pathname= os.path.normcase(os.path.realpath(pathname))
    parent_device= path_device= os.stat(pathname).st_dev
    while parent_device == path_device:
        mount_point= pathname
        pathname= os.path.dirname(pathname)
        if pathname == mount_point: break
        parent_device= os.stat(pathname).st_dev
    return mount_point

def get_mounted_device(pathname):
    "Get the device mounted at pathname"
    # uses "/proc/mounts"
    pathname= os.path.normcase(pathname) # might be unnecessary here
    try:
        with open("/proc/mounts", "r") as ifp:
            for line in ifp:
                fields= line.rstrip('\n').split()
                # note that line above assumes that
                # no mount points contain whitespace
                if fields[1] == pathname:
                    return fields[0]
    except EnvironmentError:
        pass
    return None # explicit

def get_fs_freespace(pathname):
    "Get the free space of the filesystem containing pathname"
    stat= os.statvfs(pathname)
    # use f_bfree for superuser, or f_bavail if filesystem
    # has reserved space for superuser
    return stat.f_bfree*stat.f_bsize

print(get_mount_point("/Storage/DEFENDER_SETUP_2013_PRODUCTION"))
print(get_mounted_device("/Storage/DEFENDER_SETUP_2013_PRODUCTION"))
print(get_fs_freespace("/Storage/DEFENDER_SETUP_2013_PRODUCTION"))

if (get_fs_freespace("/Storage/DEFENDER_SETUP_2013_PRODUCTION") > 5368709120000):
   sys.exit(0)
else:
   conn = MySQLdb.connect(host= "dbase.webpick.net",
                  user="admin",
                  passwd="Go512625",
                  db="Report_system")
   x = conn.cursor()

   currentTime = datetime.datetime.now()

   print "Current Jenkins Time:", currentTime

   #sql = "INSERT INTO notification_messages (id,type,timestamp,body,target,title,severity,state) VALUES('%d','%d','%s','%s','%s','%s','%d','%d')" % \
   #      (None,2,currentTime," ","972545591300","Unsufficient Disk Space",1,0)
   
   sql = "INSERT INTO notification_messages (type,target,title,severity) VALUES ('%d','%s','%s','%d')" % \
        (2,"972545591300", "Unsufficient Disk Space", 1)
   
   try:
      x.execute(sql)
      conn.commit()
   except:
      conn.rollback()

   conn.close()
   sys.exit(1)
 
