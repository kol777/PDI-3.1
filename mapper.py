#!/usr/bin/python2.7

# ambari-metrics for map reduce
# pornim serviciul si mapreduce-ul si vom avea un istoric
#
# timestamp, valori asociate fiecarei metrici -> cu algoritmul de predictie timeseries

import sys

for line in sys.stdin:

    line = line.strip()
    words = line.split()

    for word in words:
        print "%s \t %s" % (word, 1)
