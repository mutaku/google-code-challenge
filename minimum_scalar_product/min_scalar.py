#!/usr/bin/env python
# Google Code Challenge - T9 Spelling Problem
# http://code.google.com/codejam/contest/32016/dashboard#s=p0

import itertools
from time import time


def scalar(v1, v2):
    return sum(map(lambda x, y: x * y, sorted(v1), sorted(v2, reverse=True)))

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

def makeintstring(s):
    return [int(x) for x in s.split(' ')]

def generator(data):
    results = []
    for num, v1string, v2string in grouper(3, data):
        v1, v2 = map(lambda s: makeintstring(s), (v1string, v2string))
        results.append(scalar(v1, v2))
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
        resultstring = "Case #%d: %d \n" % (run, result)
        output.write(resultstring)

    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    f = raw_input("File location: ")
    run(f, f.replace(".in", ".out"))
