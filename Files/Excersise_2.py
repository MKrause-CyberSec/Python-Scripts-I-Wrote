'''Modify your first program to print count of the words
instead of percentage of the letters. In this exercise
you will get your input from a file. Case should be ignored.'''

import string

def count_Words(list):                           #I am basically using the other algorithm like asked
    word_count = {}                              #creating a dictionary called word count and sorting the
    for word in list:                            #dictionary by words
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    for word in sorted(word_count.keys()):
        print(word, word_count[word])              #printing the key and value



infile = open('data.txt',"r")                      #opening the data.txt and creating a word list
wrd_list = []
for aline in (infile):                             #I went ahead and broke open the words removing punctuation before
    words = aline.split()                          #I pass my results of the ascii letter sort to the function
    for letters in words:
        letters = str.lower(letters)               #in order to do this I had to break the words out of the list to sort
        list = []                                  #the characters
        for char in letters:
            result = ""
            if char in string.ascii_lowercase:
                result = result + char
                list.append(result)
        word = "".join(list)
        wrd_list.append(word)                       #I then build a list of words in lowercase without punctuation to
                                                    #pass to the function

count_Words(wrd_list)
infile.close()