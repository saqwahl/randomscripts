#!/usr/bin/env python
''' '''

import os
import sys
import time

inter = int(sys.argv[1])
args = sys.argv[2:]
prog = ' '.join(args)
print("Running " + prog + "!")

while True:
    os.system(prog)
    time.sleep(inter)
