__author__ = 'Robert Adinihy '

import old_checker_pro
import sys

section = ""
for x in sys.argv:
    if x[0:8] == 'section=':
        section = x[8::]
        break
print section
if section == 'QA':
     old_checker_pro.Builder_checker().QA()
elif section == 'bijo':
    old_checker_pro.Builder_checker().bijo_BHO_p()
elif section == 'chrome_32':
    old_checker_pro.Builder_checker().chrome_silicon_32()
elif section == 'chrome_64':
    old_checker_pro.Builder_checker().chrome_sillicon_64()
elif section == 'FF_S':
    old_checker_pro.Builder_checker().ff_silicon_pro()




