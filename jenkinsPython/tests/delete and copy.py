__author__ = 'User'
import os
import shutil
import distutils.core
folder = 'C:\\compilations\\websites\\installer\\installmate\\pic_builds\\versions\\2'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception, e:
        print e
source='C:\\replication\\websites\\installer\\installmate\\pic_builds\\versions\\2'
dest='C:\\compilations\\websites\\installer\\installmate\\pic_builds\\versions\\2\\'
#shutil.copy2(source,dest)
distutils.dir_util.copy_tree(source,dest)

