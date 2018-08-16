#!/usr/bin/env python
''' '''

import os
import sys

from time import time
import argparse
import csv
import logging
import simplejson as json
from slugify import slugify
import pyimgur
import re

import praw


reddit = praw.Reddit(client_id='6vzBNLu5_ZsSnA',
                     client_secret='1BKIPClcBwLu6clUOr2pN_QnZm0',
                     user_agent='PrawPic v0.1 by NL057',
                     username='sakkabc',
                     password='roskam')

imgur_id = "23673813f8f3137"
imgur_secret = "d089dfd382a036b02e68a573c1bdd636ed0f0cae"

im = pyimgur.Imgur(imgur_id)

targetdir = os.path.expanduser('~/Pictures/Imgur')

me = reddit.redditor('sakkabc')
saved = me.saved(limit=None)

for item in saved:
    if 'imgur.com' in item.url:
        title = slugify(item.title, separator="_")

        link = item.url
        if re.match('.*imgur.com/a/.*', item.url):
            album_id = link.strip().split('/')[-1]
            try:
                album = im.get_album(album_id)
            except:
                continue
            albumdir = '{!s}/{!s}'.format(targetdir, title)
            if not os.path.exists(albumdir):
                print("Creating path: %s" % albumdir)
                os.mkdir(albumdir)
            else:
                for image in album.images:
                    filename = image.link.split('/')[-1]
                    filepath = '{!s}/{!s}'.format(albumdir, filename)
                    if not os.path.isfile(filepath):
                        print("Downloading %s" % filename)
                        try:
                            image.download(path=albumdir)
                        except:
                            print("Error While Trying to Download File...")
                    else:
                        print('%s Already exists!' % filename)


        else:
            img_id = link.strip().split('/')[-1].split('.')[0]
            try:
                img = im.get_image(img_id)
            except:
                continue
            filename = title + '.' + img.link.split('.')[-1]
            if not os.path.isfile('{!s}/{!s}'.format(targetdir, filename)):
                print("Downloading %s" % filename)
                try:
                    img.download(path=targetdir, name=title)
                except:
                    print("Error While Trying to Download File...")
            else:
                print('%s Already exists!' % filename)

