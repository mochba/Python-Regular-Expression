# Read a file "mbox.txt or mbox-short.txt" and write a program to look for lines of 
# the form: "New Revision: 39772".
# Make a list of those numbers and Extract the number from each of the lines using
# a regular expression and the findall() method. Compute the average of the numbers
# and print out the average as an integer.

import re
numberlist = []
filename = input("Enter a file name :")

try:
    stream = open(filename)
    for eachline in stream:
        eachline = eachline.strip()
        number= re.findall('^New Revision: ([0-9].*)',eachline)
        if len(number) > 0:
            value = float(number[0])
            numberlist.append(value)
    print("\n",numberlist)
    print("\n'Number Revision' occurred in the text file","'",filename,"'",len(numberlist), "times","\n")
    print("The average of the numbers in the above list is",int(sum(numberlist)/len(numberlist)),"\n")    
    
except:
    print("Enter a valid file name")
    quit()






