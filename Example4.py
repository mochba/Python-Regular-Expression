# Read file to find numbers on lines that start with the string “X-” such as:
# "X-DSPAM-Confidence: 0.8475"
# Search for lines that start with 'X' followed
# by any non whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.

import re
filename = input("Enter a file :")
try:
    stream = open(filename)
    for eachline in stream:
        eachline = eachline.strip()
        # if re.search('^X-.*: [0-9.]+',eachline):
            # print(eachline)
        value = re.findall('^X-.*: ([0-9.]+)', eachline)
        # print(value) if we print this without len(value) check in the below line it will 
        # print the empty list too
        if len(value) > 0:
            print(value)

except:
    print("File not found")
    quit()

