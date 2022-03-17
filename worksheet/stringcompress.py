# def compress_string(string):
#     new_string = '' #tracks new string 
#     count = 1 # tracks letter count 
#     for i in range(len(string)):
#         a = i 
#         a += 1 
#     if string [i] == string[a]: 
#         count += 1 
#     return new_string
# print(compress_string)





# from bz2 import compress
# import string

# string = input('')
# def compress_string(string): 
#     new_string = "" #tracks new string 
#     count = 1  #tracks letter count 
#     #add first character
#     new_string += string[0]
#     for i in range (len(string)-1):
#         if string[i] == string[i+1]:
#             count += 1 #count by one 
#     else: 
#             if count == 1: 
#             #add next letter 
#                 new_string += "1"
#             new_string += string[i +1]
#             if count > 1:
#                 new_string += str(count)
#             #add next letter 
#             new_string += string[i+1]
#             count = 1
#             if count > 1: 
#                 new_string += str(count)
#             else:
#              new_string += "1"
#              return new_string
# print(string)



# def compress_string(repeat_string):     
#     for i in range(len(repeat_string)): #as long as og string
#         j = i #tracks letter next to 
#         j += 1 #adds one 
#     if repeat_string [i] == repeat_string[j]: 
#         count += 1 
#     elif(): 
#         new_string += repeat_string[::i] 
#         new_string += str(count) #convert
#         count = 1
#     elif():
#         new_string += repeat_string[i]
#         j = i
#         j -= 1 
#         if repeat_string[i] ==  repeat_string[j]:
#                 new_string += str(count)
#         else:
#                 new_string += '1' 
# #return
#     if len(new_string) > len(repeat_string):
#         print(repeat_string)
#     else: 
#         print(new_string)

# string = input("Enter a string with repeat characters\n")
# compress_string(string)