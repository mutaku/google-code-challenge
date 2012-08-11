#!/usr/bin/env python
# Google Code Challenge - Milkshakes Problem
# http://code.google.com/codejam/contest/32016/dashboard#s=p1

from time import time


def makeshakes(customers, numshakes, numcusts):
    satlist = [-1 for _ in range(0, numshakes)]
    choices = dict()
    prefs = list()

    for cust, shakelist in enumerate(customers):
        choices[cust+1] = sorted(maketuples(shakelist))
    for shake in range(1, numshakes+1):
        prefs.append(list())
        for cust in choices.keys():
            for pref in choices[cust]:
                if pref[0] == shake:
                    prefs[-1].append([cust, pref[1]])
                else:
                    pass

    cleanup(prefs, satlist)

    if all(x != -1 for x in satlist):
        return " ".join([str(y) for y in satlist])
    else:
        return "IMPOSSIBLE"

def cleanup(prefs, satlist):
    while not janitor(prefs, satlist):
        pass
    janitor(prefs, satlist, finale=True)

def janitor(prefs, satlist, finale=False):
    changes = False
    for k, shake in enumerate(prefs):
        if finale:
            if len(shake) == 1:
                satlist[k] = shake[0][1]
                satisfycustomer(shake[0][0], prefs)
            if len(shake) and all(x[1] == 1 for x in shake):
                satlist[k] = 1
                map(lambda c: satisfycustomer(c, prefs), [c[0] for c in shake])

        if not len(shake) and satlist[k] == -1:
            satlist[k] = 0
            changes = True
        elif len(shake) and all(x[1] == 0 for x in shake):
            satlist[k] = 0
            map(lambda c: satisfycustomer(c, prefs), [c[0] for c in shake])
            changes = True
        else:
            changes = True

    return changes

def satisfycustomer(cust, target):
    [[shake.remove(choice) for choice in shake if choice[0] == cust] for shake in target]
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
