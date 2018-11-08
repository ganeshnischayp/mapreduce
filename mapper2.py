#!/usr/bin/env python
import sys
for line in sys.stdin:
    num = line.split(",")[1]
    document = line.split(",")[0].split("@")[1]
    word = line.split(",")[0].split("@")[0]
    sys.stdout.write("{0},{1}={2}".format(document, word, num))
