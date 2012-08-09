#!/usr/bin/env python
# Google Code Challenge - Milkshakes Problem
# http://code.google.com/codejam/contest/32016/dashboard#s=p1

from time import time


def makeshakes(data):
    # code me please!
    pass

def generator(data):
    results = list()
    cases = int(data.next())

    for case in cases:
        while 1:
            N, M = [data.next() for _ in range(2)]
            results.append(makeshakes([data.next() for _ in range(0, int(M))]))
            break

    return results

def run(data_file, output_file):
    data = open(data_file)
    output = open(output_file, 'w')

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
