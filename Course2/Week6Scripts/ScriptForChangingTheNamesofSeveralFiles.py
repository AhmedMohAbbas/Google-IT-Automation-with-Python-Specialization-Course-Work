#! python

import sys
import subprocess

x = sys.argv[1]

with open(x, 'r') as fh:
    for line in fh:
        oldname = line.strip()
        newname = oldname.replace("jane","jdoe")
        subprocess.run(['mv', oldname, newname])