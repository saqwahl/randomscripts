#!/usr/bin/env python
''' '''

import os
import sys
import time

args = sys.argv[1:]
prog = ' '.join(args)
print("Running " + prog + "!")

while True:
    os.system(prog)
    time.sleep(3)
