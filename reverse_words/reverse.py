#!/usr/bin/env python
# Google Code Challenge - Reverse Words Problem
# http://code.google.com/codejam/contest/351101/dashboard#s=p1

from time import time

def flipflopper(data):
    # Flipflop our data
    results = []
    # Iterate over lines and generate inverse
    for line in data:
        # Strip off newline characters
        line.rstrip('\n')
        # Split on spaces and then reverse the list
        results.append(line.split(" ")[::-1])
    return results

def run(data_file, output_file):
    # Establish input/output files
    data = open(data_file)
    output = open(output_file, 'w')
    # First line of file (number cases) is not important
    data.next()

    # Run our program and time execution (lazy way)
    start = time()
    results = flipflopper(data)
    end = time()
    complete = end - start

    # Write results to our output file
    for run, result in enumerate(results, start=1):
        resultstring = "Case #%d: %s \n" % (run, " ".join(result))
        output.write(resultstring)

    # Close file objects and print time to stdout
    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    # If executed as main, we need to grab input file
    f = raw_input("File location: ")
    run(f, f.replace(".in", ".out"))
