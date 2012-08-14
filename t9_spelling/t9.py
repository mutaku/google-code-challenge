#!/usr/bin/env python
# Google Code Challenge - T9 Spelling Problem
# http://code.google.com/codejam/contest/351101/dashboard#s=p2

from time import time

# Keypad translation
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

# Setup mapper for which number to dial and how many times for each char
dial = {}
for digit in keypad.keys():
    for char in keypad[digit]:
        dial[char] = (digit, keypad[digit].index(char))

def sendtext(data):
    # Send our text message
    results = []
    for line in data:
        action = []
        # We don't use 1 so we make that our initial holder value
        last_button = 1
        # Strip off newline characters from each line and iterate over chars
        for char in line.rstrip('\n'):
            # Find out which button to push and how many times for this char
            button, push = dial[char]
            # If we already used a char mapped to this button, add a pause
            if button == last_button:
                action.append(" ")
            else:
                pass
            # Add our necessary button push to the action and push it that number times
            action.append(str(button) * (push + 1))
            # Set our last button tracker to this one
            last_button = button
        results.append(action):
    return results

def run(data_file, output_file):
    # Establish input/output files
    data = open(data_file)
    output = open(output_file, 'w')
    # First line of file (number cases) is not important
    data.next()

    # Run our program and time execution (lazy way)
    start = time()
    results = sendtext(data)
    end = time()
    complete = end - start

    # Write results to our output file
    for run, result in enumerate(results, start=1):
        resultstring = "Case #%d: %s \n" % (run, "".join(result))
        output.write(resultstring)

    # Close file objects and print time to stdout
    data.close()
    output.close()
    print "Computed %s and wrote %s taking %f s" % (data_file, output_file, complete)

if __name__ == "__main__":
    # If executed as main, we need to grab input file
    f = raw_input("File location: ")
    run(f, f.replace(".in", ".out"))
