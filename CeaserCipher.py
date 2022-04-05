'''Please develop a program to help you crack the following secret message.
For the encryption we have used simple Caesar cipher. You can find more information
on https://en.wikipedia.org/wiki/Caesar_cipher. Write a function to decrypt the message.
The function must have offset value, input file and output file parameters.  The offset
value is the number n as described in the wiki.  No global variables are used in the function.
Function parameters must be used.'''
import string

#offset value for ceaser cipher is n = (-17)

def decrypt(ifile):
    for line in ifile:
        letters = line.split()
        letters = "".join(letters)       #letters must be converted to string format to do the encryption
        new_list = []                    #created a list to hold our new elements
        for char in letters:
            result = ""
            if char in string.ascii_uppercase:
                idx = string.ascii_uppercase.find(char)
                result = result + string.ascii_uppercase[idx - 17]   #checked against the ascii table the -17 is the n offset value
                new_list.append(result)                              #I orginally checked against ascii_letters but you dont
                                                                     #get the correct output that way
            elif char in string.ascii_lowercase:
                idx = string.ascii_lowercase.find(char)
                result = result + string.ascii_lowercase[idx - 17]
                new_list.append(result)

            else:
                char not in string.ascii_letters                     #I think it is important for me to note that PyCharm
                result = result + char                               #tells me I don't have to make that last check
                new_list.append(result)                              #but if I don't I get an incorrect output
                                                                     #you may have show us a better method for that
        outfile.write("".join(new_list) + '\n')                      #but it is like finding a needle in a haystack at
                                                                     #times

infile = open('encrypted',"r")
outfile = open('decrypted',"w")
decrypt(infile)

infile.close()
outfile.close()
