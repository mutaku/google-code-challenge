#!/usr/bin/env python
# Google Code Challenge - Milkshakes Problem
# http://code.google.com/codejam/contest/32016/dashboard#s=p1

from time import time


def makeshakes(customers, numshakes, numcusts):
    # code me please!
    unsatlist = list()
    satlist = list()
    choices = dict()

    for cust, shakelist in enumerate(customers):
        choices[cust] = sort(maketuples(shakelist))

    for shake in numshakes:
        unsatlist.append(list())
        prefs = list()
        for cust in choices.keys():
            for pref in choices[cust]:
                if pref[0] == shake:
                    prefs.append((cust, pref[1]))
                    break
                else:
                    pass

        matching = True
        for k, v in enumerate(prefs):
            if k > 0 and v[1] != prefs[k-1][1]:
                matching = False
        custlist = [x for x, y in prefs]
        if not matching:
            unsatlist[-1] = custlist
        else:
            map(lambda c: satisfycustomer(c, unsatlist), custlist)

    # now we have to build our to make list for shakes
    # this will be our sat list

    if satlist:
        result = " ".join([str(y) for y in sum([x for x in satlist], [])])
    else:
        result = "IMPOSSIBLE"
    return result

def satisfycustomer(cust, unsatlist):
    map(lambda l: l.remove(cust), [sub for sub in unsatlist if cust in sub])

def checkpossibility(unsatlist):
    if len(sorted(unsatlist, key=len, reverse=True)[0]) > 1:
        return False
    else:
        return True

def maketuples(string):
    values = [int(x) for x in string.split(" ")]
    return [values[i:i+2] for i in range(o, len(values), 2)]

def generator(data):
    results = list()
    cases = int(data.next())

    for case in cases:
        while 1:
            N, M = [data.next() for _ in range(2)]
            results.append(makeshakes([data.next() for _ in range(0, int(M))],N, M))
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
