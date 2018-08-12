#!/usr/bin/env python
''' '''

import os
import sys
import random

abs = os.path.abspath
pics = os.listdir(os.path.expanduser('~/Pictures/Wallpapers'))
for pic in pics:
    abs(pic)


random_index = random.randrange(0, len(pics))

print(pics[random_index])
# os.system('ls -l')

# wallpic = pics[random_index]
# command = 'feh --fill-bg' + str(wallpic)
# os.system(command)

