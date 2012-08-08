#!/usr/bin/env python
# Google Code Challenge - Milkshakes Problem
# http://code.google.com/codejam/contest/32016/dashboard#s=p1

import itertools
from time import time


def makeshakes(data):
    pass

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

def generator(data):
    results = []
    # have to group based on each case since we will have M lines for M customers
    # parse first two lines to get N shakes and M customers and then grab customer profiles by grouper(M, data)
    return results

def run(data_file, output_file):
    data = open(data_file)
    output = open(output_file, 'w')
    data.next()

    start = time()
    results = generator(data)
    end = time()
    complete = end - start

    for run, result in enumerate(results, start=1):
        resultstring = "Case #%d: %s \n" % (run, " ".join(result))
        output.write(resultstring)

    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    f = raw_input("File location: ")
    run(f, f.replace(".in", ".out"))
