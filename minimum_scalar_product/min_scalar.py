#!/usr/bin/env python
# Google Code Challenge - Minimum Scalar Product Problem
# http://code.google.com/codejam/contest/32016/dashboard#s=p0

import itertools
from time import time


def scalar(v1, v2):
    # Find lowest scalar product sum
    # Sort asc one vector, sort desc the other, and operate
    return sum(map(lambda x, y: x * y, sorted(v1), sorted(v2, reverse=True)))

def grouper(n, iterable, fillvalue=None):
    # Cluster data by iterating over lines of a file object
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

def makeintstring(s):
    # Create a list of ints from string
    return [int(x) for x in s.split(' ')]

def generator(data):
    # Parse input file, cluster data, and run our algorithm on it
    results = []
    for num, v1string, v2string in grouper(3, data):
        # Read in second and third lines and convert to lists of ints
        v1, v2 = map(lambda s: makeintstring(s), (v1string, v2string))
        # Run scalar algorithm on vectors
        results.append(scalar(v1, v2))
    return results

def run(data_file, output_file):
    # Establish input/output files
    data = open(data_file)
    output = open(output_file, 'w')
    data.next()

    # Run our program and time execution (lazy way)
    start = time()
    results = generator(data)
    end = time()
    complete = end - start

    # Write results to our output file
    for run, result in enumerate(results, start=1):
        resultstring = "Case #%d: %d \n" % (run, result)
        output.write(resultstring)

    # Close file objects and print time to stdout
    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    # If excuted as main, we need to grab input file
    f = raw_input("File location: ")
    run(f, f.replace(".in", ".out"))
