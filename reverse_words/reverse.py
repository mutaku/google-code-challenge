#!/usr/bin/env python
# Google Code Challenge - Reverse Words Problem
# http://code.google.com/codejam/contest/351101/dashboard#s=p1

from time import time

def flipflopper(data):
    results = []
    for line in data:
        line.rstrip('\n')
        results.append(line.split(" ")[::-1])
    return results

def run(data_file, output_file):
    data = open(data_file)
    output = open(output_file, 'w')
    data.next()

    start = time()
    results = flipflopper(data)
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
