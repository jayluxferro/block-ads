#!/usr/bin/env python3

import sys


def usage():
    print('Usage: python {} [path_to_ad_list]'.format(sys.argv[0]))
    sys.exit(1)



if len(sys.argv) != 2:
    usage()


data = [ x.rstrip().strip() for x in open('./list.txt', 'r').readlines() ]

for _data in open(sys.argv[1], 'r').readlines():
    _url = _data.rstrip().strip()
    try:
        data.index(_url)
    except:
        print(_url)
