# !/usr/bin/env python

import sys


def is_validation_numbers():
    return True if len(sys.argv) == 2 and \
                   int(sys.argv[1]) > 0 else False
