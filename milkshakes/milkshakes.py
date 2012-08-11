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
        choices[cust+1] = sorted(maketuples(shakelist))
    for shake in range(1, numshakes+1):
        unsatlist.append(list())
        prefs = list()
        for cust in choices.keys():
            for pref in choices[cust]:
                if pref[0] == shake:
                    prefs.append([cust, pref[1]])
                    break
                else:
                    pass

        matching = True
        if len(prefs):
            for k, v in enumerate(prefs):
                if k > 0 and v[1] != prefs[k-1][1]:
                    matching = False
                else:
                    pass
        else:
            pass

        if not matching:
            satlist.append(0)
            unsatlist[-1] = prefs
        elif matching and not len(prefs):
            satlist.append(0)
        else:
            satlist.append(prefs[0][1])
            map(lambda c: satisfycustomer(c, unsatlist, choices), [cust[0] for cust in prefs])

    if checkpossibility(unsatlist, satlist):
        return " ".join([str(y) for y in satlist])
    else:
        #return str(unsatlist)
        return "IMPOSSIBLE"

def satisfycustomer(cust, unsatlist, choices):
    [[shake.remove(choice) for choice in shake if choice[0] == cust] for shake in unsatlist]
    del choices[cust]
    return True

def checkpossibility(unsatlist, satlist):
    if len(sorted(unsatlist, key=len, reverse=True)[0]) > 1:
        return False
    else:
        for k, v in enumerate(unsatlist):
            if len(v):
                satlist[k] = v[0][1]
        return True

def maketuples(string):
    values = [int(x) for x in string.split()[1:]]
    return [values[i:i+2] for i in range(0, len(values), 2)]

def generator(data):
    results = list()
    cases = int(data.next())

    for case in range(0, cases):
        while 1:
            totalshakes, totalcust = [int(data.next()) for _ in range(2)]
            results.append(makeshakes([data.next() for _ in range(0, totalcust)], totalshakes, totalcust))
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
        resultstring = "Case #%d: %s\n" % (run, result)
        output.write(resultstring)

    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    f = raw_input("File location: ")
    run(f, f.replace(".in", ".out"))
