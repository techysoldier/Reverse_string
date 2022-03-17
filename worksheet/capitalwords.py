# Input lower case 
# Output upper case
# cap current index
# if index -1 is space cap current  
# append
#return cap selection 
#print cap format 



def cap_letter(str):
    cap_words = str[0].upper()
    for i in range(1, len(str)):
        if (str[i-1] == " "):
            cap_words += str[i].upper()
        else:
            cap_words += str[i]
    return cap_words

print(cap_letter("hello world it's me"))