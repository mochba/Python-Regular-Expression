# Read file to find numbers on lines that start with the string “Details:-” such as:
# "Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772"
# Search for lines that start with 'Details:' followed
# by any non whitespace characters and 'rev' We want to find lines that match the 
# entire expression but we only want to extract the integer number at the end of the 
# line, so we surround [0-9]+ with parentheses.

import re

filename = input("Enter a file name:")

try:
    stream = open(filename)
    for eachline in stream:
        eachline = eachline.strip()
        value = re.findall('^Details: .*rev=([0-9].+)',eachline)
        if len(value) > 0: 
            print(value)
except:
    print("Enter a vaild file name")
    quit()

