# Find a line given below from the file mbox-short.txt or mbox.txt
# "BY dreamcatcher.mr.itd.umich.edu ID 477E9B13.2F3BC.22965 ;"
# extract only text before import ipdb; ipdb.set_trace()

import re

filename = input("Enter a file name :")

try:
    stream = open(filename)

    for eachline in stream:
        eachline = eachline.strip()
        words = re.findall('([a-z.]+) ID',eachline)
        if len(words) > 0:
            print(words)
except:
    print("Enter a correct the file name")
    quit()



# s= "BY dreamcatcher.mr.itd.umich.edu ID 477E9B13.2F3BC.22965 ;"
# d = re.findall('[a-z]',s)
# print(d)
#       ['d', 'r', 'e', 'a', 'm', 'c', 'a', 't', 'c', 'h', 'e', 'r', 'm', 'r', 'i', 
#       't', 'd', 'u', 'm', 'i', 'c', 'h', 'e', 'd', 'u']

# d = re.findall('[a-z].',s)
# ['dr', 'ea', 'mc', 'at', 'ch', 'er', 'mr', 'it', 'd.', 'um', 'ic', 'h.', 'ed', 'u ']

# d = re.findall('[a-z]+',s)
# ['dreamcatcher', 'mr', 'itd', 'umich', 'edu']

# d = re.findall('.',s)
# ['B', 'Y', ' ', 'd', 'r', 'e', 'a', 'm', 'c', 'a', 't', 'c', 'h', 'e', 'r', '.', 
# 'm', 'r', '.', 'i', 't', 'd', '.', 'u', 'm', 'i', 'c', 'h', '.', 'e', 'd', 'u', ' ', 
# 'I', 'D', ' ', '4', '7', '7', 'E', '9', 'B', '1', '3', '.', '2', 'F', '3', 'B', 'C', 
# '.', '2', '2', '9', '6', '5', ' ', ';']

# d = re.findall('.+',s)
# ['BY dreamcatcher.mr.itd.umich.edu ID 477E9B13.2F3BC.22965 ;']

# d = re.findall('[a-z]+.',s)
# ['dreamcatcher.', 'mr.', 'itd.', 'umich.', 'edu ']

# d = re.findall('[a-z]+. ID',s)
# ['edu ID']

# d = re.findall('[a-z]+.',s)
# ['dreamcatcher.', 'mr.', 'itd.', 'umich.', 'edu ']

# d = re.findall('[a-z.]+ ID',s)
# ['dreamcatcher.mr.itd.umich.edu ID']

# d = re.findall('([a-z.]+) [ID]',s)
# ['dreamcatcher.mr.itd.umich.edu']






