# Read a file "mbox-short.txt and search for lines that start with From and a character
# like "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008m"
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero

import re
filename = input("Enter a file name:")

try:
    stream = open(filename)
    for eachline in stream:
        eachline = eachline.strip()
        # hour = re.findall('^From .* [0-9][0-9]:',eachline) try running and check
        # hour = re.findall('^From .* ([0-9][0-9]):',eachline)try running and check
        hour = re.findall('^From .* ([0-9][0-9]):',eachline)
        if len(hour) > 0:
            print(hour)
except:
    print("Enter a valid file")
    quit()
