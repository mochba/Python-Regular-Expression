import re
count  = 0 
filename = input("Enter a file name:")

try:
    stream = open(filename)
    for eachline in stream:
        eachline =  eachline.rstrip()
        
        if re.search('^From:.+@',eachline):
            print(eachline)
        x = re.findall('\S+@\S+', eachline)
        if len(x) > 0:
            count = count+1
            print("\t","\S+@\S+","\t" ,count, x)
        y = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', eachline)
        if len(y) > 0:
            print("\t\t","[a-zA-Z0-9]\S+@\S+[a-zA-Z]","\t\t",count,y)
    print("Number of email id in the file is ", count)
except:
    print("Enter a correct file name")
    quit()