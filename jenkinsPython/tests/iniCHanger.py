import os
import sys
import glob
ini_list = []

for root, directories, files in os.walk(os.getcwd()):
    for filename in files:
        path = sys.argv[2]
        #print path
        #'/nas/QA/Robert/Robert/regresion exstention/'
        #filepath = path.join(root, filename)
        #print filepath
        #print path
        #if root ==path and filename.endswith(".ini"):
        ini_list= glob.glob(path +"*.ini")

print ini_list

link = sys.argv[1]
print link
for x in ini_list:
    f = open(x, "r")

    content = f.readlines()
    array = []
    for line in content:
        if line[0:4] == "URl=":
            line = "URl=" +link
        array.append(line)

    f.close()

    a = open(x, "wb")
    for x in array:
        a.write(x)
        a.write("\r\n")

    a.close()