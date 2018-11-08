#!/usr/bin/env python
import sys
for line in sys.stdin:
    document = line.strip().split("@")[0]
    word = line.strip().split("@")[1].split(",")[0]
    freq = line.strip().split(",")[1]
    sys.stdout.write("{0},{1}={2}\n".format(word, document, freq))
