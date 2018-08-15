#!/usr/bin/env python
''' '''

import os
import sys
import random
import minidb

dbfile = os.path.expanduser('~/.walldb')
print(dbfile)
db = minidb.Store(dbfile, debug=True)
print(db)

class Picture(minidb.Model):
    id = int
    imgname = str


db.register(Picture)






































































# abs = os.path.abspath
# pics = os.listdir(os.path.expanduser('~/Pictures/Wallpapers'))
# for pic in pics:
#     abs(pic)

# random_index = random.randrange(0, len(pics))
# print('[ %s ]' % random_index + ' === ' + pics[random_index])
# wallpic = os.path.expanduser("~/Pictures/Wallpapers/%s" % pics[random_index])
# print(wallpic)
# command = 'feh --bg-fill %s' % wallpic
# print(command)
# os.system(command)

