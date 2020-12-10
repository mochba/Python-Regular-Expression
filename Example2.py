# import re
# count = 0
# filename = input("Enter a file name:")

# try:
#     stream = open(filename)
#     for eachline in stream:
#         eachline = eachline.rstrip()
#         if re.search("^F..m: ",eachline):
#             print(eachline)
#             count = count+1
#     print("Number of email id in the file is ", count)
# except:
#     print("Entered file is not found")
#     quit()


# a = [1, 2, 9, 3, 4]
# a = nums[:4]
# for i in a:
#     if a[i] == 9:
#         return True
#     else:
#       return False

def round_sum(a, b, c):
  a_len = len(str(a))
  if a_len >= 2:
    a_tens = modify_10s(a)
    a =  str(a)
    a_ones = change_value(int(a[1:]))
    a_final = a_tens + a_ones 
  else:
    a_final = change_value(a)
    
  b_len = len(str(b))
  if b_len >= 2:
    b_tens = modify_10s(b)
    b =  str(b)
    b_ones = change_value(int(b[1:]))
    b_final = b_tens + b_ones 
  else:
    b_final = change_value(b)
    
    
  c_len = len(str(c))
  if c_len >= 2:
    c_tens = modify_10s(c)
    c =  str(c)
    c_ones = change_value(int(c[1:]))
    c_final = c_tens + c_ones 
  else:
    c_final = change_value(c)
    
  return a_final + b_final + c_final  
  
def change_value(num):
  if num >= 5 and num <= 9:
    return 10
  else:
    return 0

def modify_10s(num):
  num_str = str(num)
  return int(num_str[:1]) * 10

l= round_sum(0,0,1) 
print(l)