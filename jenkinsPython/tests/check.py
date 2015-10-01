

 def check():
        datafile = file('/nas/QA/Robert/html/python/bob10.txt')
        found = False
        s='Netscape 5-succses'
        for line in datafile:
            if s in line:
                found = True
              break

check()
if True:
    print "true"
else:
    print "false"