#!/usr/bin/env python
''' '''

import sys
import os
from qbittorrent import Client
import simplejson as json
import colorama
import termcolor
import re

qb = Client('http://127.0.0.1:8080/')

qb.login('admin', 'kankerlelijk')

torrents = qb.torrents()

# print(json.dumps(torrents[0], sort_keys=True, indent=4 * ' '))


torfiles = dict()
regex = str(sys.argv[1])

for torrent in torrents:
    name = torrent['name']
    files = qb.get_torrent_files(torrent['hash'])
    filenames = list()

    for file in files:
        n = file['name']
        if n.endswith('.mp4') or n.endswith('.mkv'):
            filenames.append(file['name'])

    torfiles[name] = filenames

    # print(torfiles)
    # print(torrent['hash'])
    # print(json.dumps(torfiles, sort_keys=True, indent=4 * ' '))

    for key in torfiles.keys():
        flist = torfiles[key]
        matches = 0
        matcheditems = list()
        for item in flist:
            if re.search(regex, item, re.IGNORECASE):
                matcheditems.append(item)
                matches += 1
        if matches >= 1:
            print(termcolor.colored('\n\n' + key.upper(), 'green'))
            for item in matcheditems:
                print(item)





        # if matches < 1:
        #     print(termcolor.colored("\tNothing Found!!!", 'red'))

