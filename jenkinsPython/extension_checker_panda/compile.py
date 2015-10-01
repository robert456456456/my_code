from distutils.core import setup
from glob import glob
import py2exe



datafiles = [("", ["D:\\qa-automation\\jenkinsPython\\extension_checker_panda\\cfg.ini"])]

"""
example
#datafiles = [('folder Name', [lists of paths of files to copy to that folder])]
if you want to include all files in certain folder use the following:
fileslist = glob("c:\\robert\\is\\gay\\*.*")
fileslist2 = glob("c:\\robert\\is\\baran\\*.*")

datafiles = [("robert the gay", fileslist), ("robert the baran", fileslist2)]
this will create a folder called "robert the gay" and will copy there all the files from c:\\robert\\is\\gay
will also create another folder called "robert the baran" and will copy there all the files from the folder c:\\robert\\is\\baran

"""


setup(
    console=['old_checker.py'], #use windows= instead of console= if you want the program to work without a cmd window (might be less stable)
    data_files = datafiles,
    options={
        "py2exe":{
            "optimize": 2, #if compilation doesn't work change value to 0
            "includes": [], #add names of all libraries you import
            "bundle_files": 3 #change value to 1 or 2 if you want less files in the package, be aware that it might cause the compilation not to work.

        }

    },
    zipfile = None



)