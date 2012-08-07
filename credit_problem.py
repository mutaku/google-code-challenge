#!/usr/bin/env python
# Google Code Challenge - Credit Problem
# http://code.google.com/codejam/contest/351101/dashboard#s=p0

import itertools
import bisect
from time import time


def last(array, num):
    return (len(array) - 1) - array[::-1].index(num)

def check(items, credit):
    orig = list(items)
    items.sort()
    items = items[:bisect.bisect_right(items, credit)]
    if len(items) == 2:
        return items
    else:
        for i in items:
            mine = items.index(i)
            try:
                leaf = items[bisect.bisect_left(items, credit/2):]
                yours = last(leaf, credit - i)
                found = [orig.index(i) + 1, last(orig, credit - i) + 1]
                found.sort()
                return found
                break
            except:
                pass

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

def generator(data):
    results = []
    for creditstring, num, itemstring in grouper(3, data):
        items = [int(x) for x in itemstring.split(' ')]
        credit = int(creditstring)
        results.append(check(items, credit))
    return results

def run(data_file, output_file):
    data = open(data_file)
    output = open(output_file, 'w')
    data.next()

    start = time()
    results = generator(data)
    end = time()
    complete = end - start

    for run, result in enumerate(results):
        resultstring = "Case #%d: %s \n" % (run + 1, " ".join([str(x) for x in result]))
        output.write(resultstring)

    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    f = raw_input("File location: ")
    run(f, f.rstrip('.in')+'.out')
