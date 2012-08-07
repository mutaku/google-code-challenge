#!/usr/bin/env python
# Google Code Challenge - Credit Problem
# http://code.google.com/codejam/contest/351101/dashboard#s=p0

import itertools
from time import time

def check(items, credit):
    for i in items:
        mine = items.index(i)
        try:
            yours = (len(items) - 1) - items[::-1].index(credit - i)
            if mine != yours:
                return [mine+1, yours+1]
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
    # first line in this problem is not needed
    data.next()

    start = time()
    results = generator(data)
    end = time()
    complete = end - start

    for run, result in enumerate(results):
        resultstring = "Case #%d: %s " % (run, " ".join([str(x) for x in result]))
        output.write(resultstring)

    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    f = raw_input("File location: ")
    run(f, f.rstrip('.in')+'.out')