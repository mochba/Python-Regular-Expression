# Exercise 1: Write a simple program to simulate the operation of the grep command 
# on Unix. Ask the user to enter a regular expression and count the number of lines
# that matched the regular expression:

import re

filename  = input("Enter a file name:")
count = 0
try:
    stream = open(filename)
    regular_expression = input("Enter a regular expression:")
    for eachline in stream:
        eachline = eachline.rstrip()
        if re.findall(regular_expression,eachline):
            count = count + 1
    print("File name","'", filename,"'", "has", "'",regular_expression,"'", count ,"times")
except:
    print("Enter a valid file name")
    quit()



