#!/usr/bin/env python
# Google Code Challenge - Milkshakes Problem
# http://code.google.com/codejam/contest/32016/dashboard#s=p1

from time import time


def makeshakes(customers, numshakes, numcusts):
    # Setup iterators and find out what shakes we are going to make
    satlist = [-1 for _ in range(0, numshakes)]
    choices = dict()
    prefs = list()

    # Build customer preference data holder
    for cust, shakelist in enumerate(customers):
        choices[cust+1] = sorted(maketuples(shakelist))
    # Find out preferences for each customer for each shake we are making
    for shake in range(1, numshakes+1):
        prefs.append(list())
        for pref in [choices[cust] for cust in choices.keys()]:
            if pref[0] == shake:
                prefs[-1].append([cust, pref[1]])
            else:
                pass

    # Run our satisfiability algorithm through our workflow handler
    # This will handle primary and secondary condition scenarios
    janitor(prefs, satlist)

    # If we've been able to make all shakes, return them as a string
    # Else, this is impossible
    if all(x != -1 for x in satlist):
        return " ".join([str(y) for y in satlist])
    else:
        return "IMPOSSIBLE"

def janitor(prefs, satlist):
    # Loop over prefs and run our satisfiability algorithm
    # We run this until we don't make any further changes
    while cleanup(prefs, satlist):
        pass
    # Now we loop over with our secondary conditions
    while cleanup(prefs, satlist, finale=True):
        pass

def cleanup(prefs, satlist, finale=False):
    # The actual satisfiability algorithm in action
    changes = False
    # Iterate over each shake's preferences
    for k, shake in enumerate(prefs):
        # Initial conditions to try and find unmalted satisfactory scenarios
        # Not requested and we haven't set it yet, we make unmalted
        if not len(shake) and satlist[k] == -1:
            satlist[k] = 0
            changes = True
        # All preferences are for unmalted, make unmalted and satisfy all customers here
        elif len(shake) and all(x[1] == 0 for x in shake):
            satlist[k] = 0
            map(lambda c: satisfycustomer(c, prefs), [c[0] for c in shake])
            changes = True

        # Loop over with secondary conditions
        if finale:
            # If only one preference, we have to satisfy this customer
            if len(shake) == 1:
                satlist[k] = shake[0][1]
                satisfycustomer(shake[0][0], prefs)
                changes = True
            # If everyone is malted, we make malted
            elif len(shake) and all(x[1] == 1 for x in shake):
                satlist[k] = 1
                map(lambda c: satisfycustomer(c, prefs), [c[0] for c in shake])
                changes = True
            # Look for our stereoisomers and satisfy
            elif len(shake) > 1 and doesflipflop(shake, prefs, satlist):
                map(lambda c: satisfycustomer(c, prefs), [c[0] for c in shake])

    return changes

def doesflipflop(shake, prefs, satlist):
    # Look for stereoisomers in our data
    # These would be something like A-> (1,0)(2,1) B-> (1,1)(2,0)
    testcase = []
    # Translation mapper
    flipper = {0: 1, 1: 0}
    # Build our isomer for each preference
    for choice in shake:
        testcase.append([choice[0], flipper[choice[1]]])
    # Iterate over other shake preferences and try to find our isomer
    # If one exists,  we set both to unmalted since we know they will be happy with either
    # Return True or False so we know if we've found one
    if testcase in prefs:
        satlist[prefs.index(testcase)] = 0
        satlist[prefs.index(shake)] = 0
        return True
    else:
        return False

def satisfycustomer(cust, target):
    # Iterate of preferences list and suck out any that contain our customer
    # This customer has been satisfied and we no longer want to account for him/her
    [[shake.remove(choice) for choice in shake if choice[0] == cust] for shake in target]
    return True

def maketuples(string):
    # Turn our string list into integers
    # Skip first value which is total preferences for this customer
    values = [int(x) for x in string.split()[1:]]
    # Assemble data like [shake, malt preference]
    return [values[i:i+2] for i in range(0, len(values), 2)]

def generator(data):
    # Parse input file and cluster data by case
    # Feed clustered data to our algorithm
    results = list()
    # Read first line of file as total number cases
    cases = int(data.next())

    for case in range(0, cases):
        # Collect relevant data for this case
        while 1:
            # Read in next two lines for total shakes and customers
            totalshakes, totalcust = [int(data.next()) for _ in range(2)]
            # Read in each customers preference string and run all data through algorithm
            results.append(makeshakes([data.next() for _ in range(0, totalcust)], totalshakes, totalcust))
            # Next customer
            break

    return results

def run(data_file, output_file):
    # Establish input/output files
    data = open(data_file)
    output = open(output_file, 'w')

    # Run our program and time execution (lazy way)
    start = time()
    results = generator(data)
    end = time()
    complete = end - start

    # Write results to our output file
    for run, result in enumerate(results, start=1):
        resultstring = "Case #%d: %s\n" % (run, result)
        output.write(resultstring)

    # Close file objects and print time to stdout
    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    # If executed as main, we need to grab input file
    f = raw_input("File location: ")
    run(f, f.replace(".in", ".out"))
