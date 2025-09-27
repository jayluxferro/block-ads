#!/usr/bin/env python3

import sys


def usage():
    print(f"Usage: {sys.argv[0]} <host_block_file>")
    sys.exit(1)


if len(sys.argv) != 2:
    usage()

data = [f"0.0.0.0 {host.rstrip().strip()}" for host in open(sys.argv[1]).readlines()]
print("\n".join(data))
