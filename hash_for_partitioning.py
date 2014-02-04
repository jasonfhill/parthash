#!/usr/bin/env python
""" Simple test of hashing for use
    with load balancing or partitioning"""

import hashlib
import string
import random

SERVER_COUNT = 3

def create_random_string(size=32, char=string.ascii_letters + string.digits):
    """Generate random string"""
    return ''.join(random.choice(char) for i in range(size))

RANDOM_STRING = create_random_string()
HASHED = int(hashlib.md5(RANDOM_STRING.encode('utf-8')).hexdigest(), 32)

print "%s is on server %s" % (RANDOM_STRING, HASHED % SERVER_COUNT)
