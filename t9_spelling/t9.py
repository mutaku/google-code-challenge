#!/usr/bin/env python
# Google Code Challenge - T9 Spelling Problem
# http://code.google.com/codejam/contest/351101/dashboard#s=p2

from time import time

keypad = {
        0: [' '],
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']}

dial = {}

for digit in keypad.keys():
    for char in keypad[digit]:
        dial[char] = (digit, keypad[digit].index(char))

def sendtext(data):
    results = []
    for line in data:
        action = []
        last_button = 1
        for char in line.rstrip('\n'):
            button, push = dial[char]
            if button == last_button:
                action.append(" ")
            else:
                pass
            action.append(str(button) * (push + 1))
            last_button = button
        results.append(action)
    return results

def run(data_file, output_file):
    data = open(data_file)
    output = open(output_file, 'w')
    data.next()

    start = time()
    results = sendtext(data)
    end = time()
    complete = end - start

    for run, result in enumerate(results, start=1):
        resultstring = "Case #%d: %s \n" % (run, "".join(result))
        output.write(resultstring)

    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    f = raw_input("File location: ")
    run(f, f.replace(".in", ".out"))
