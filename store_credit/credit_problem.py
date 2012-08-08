#!/usr/bin/env python
# Google Code Challenge - Credit Problem
# http://code.google.com/codejam/contest/351101/dashboard#s=p0

import itertools
import bisect
from time import time


def check(items, credit):
    orig = list(items)
    items.sort()
    extsplice = bisect.bisect_left(items, credit)
    intsplice = bisect.bisect_right(items, credit/2)
    leftleaf, rightleaf = items[:intsplice], items[intsplice:extsplice]
    for i in leftleaf:
        try:
            (len(rightleaf) - 1) - rightleaf[::-1].index(credit - i)
            last_element = (len(orig) - 1) - orig[::-1].index(credit - i)
            found = sorted([orig.index(i) + 1, last_element + 1])
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

    for run, result in enumerate(results, start=1):
        resultstring = "Case #%d: %s \n" % (run, " ".join([str(x) for x in result]))
        output.write(resultstring)

    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    f = raw_input("File location: ")
    run(f, f.rstrip('.in')+'.out')
