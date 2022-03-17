from bz2 import compress
import string

def compress_string(string): 
    new_string = "" #tracks new string 
    count = 1  #tracks letter count 
    #add first character
    new_string += string[0]
    for i in range (len(string)-1):
        if string[i] == string[i+1]:
            count += 1 #count by one 
    else: 
            if count == 1: 
            #add next letter 
                new_string += 1
            new_string += string[i +1]
            if count > 1:
                new_string += str(count)
            #add next letter 
            new_string += string[i+1]
            count = 1
            if count > 1: 
                new_string += str(count)
            else:
             new_string += "1"
             return new_string

string_status = compress_string(input('enter word'))
print (string_status)