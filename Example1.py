import re
count = 0
try:
    stream =  open(input("Enter a file name:"))
    for eachline in stream:
        eachline = eachline.rstrip()
        if re.search("From: ",eachline):
            print(eachline)
            count = count+1
    print("Number of email id in the file is ", count)
except:
    print("file name is not found")
    quit()




