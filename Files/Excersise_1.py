'''Develop a program that asks the user to enter a text.
The program should analyze the text and print out unique letters,
in alphabetical order, with the percentage information of each letter.
Case should be ignored.  Write a function to analyze the text string.
No global variables are used in the function.  Function parameters must be used.'''


import string

def count_letters(str):
    letter_count = {}
    str = str.lower()
    for char in str:
        if char in string.ascii_lowercase:                 # I used the code we developed in class to look for lowercase letters
            if char in letter_count:
                letter_count[char] = letter_count[char] +1
            else:
                letter_count[char] = 1

    theSum = 0                                             #in order to get any percentage we need the total of the values
    for num in list(letter_count.values()):                #you have to use an accumulator and hold the total in the variable theSum
        theSum = theSum + num

    for char in sorted(letter_count.keys()):
        print(char, "{0:.1F}".format((letter_count[char] / theSum) * 100) ,"%")          #formatting the output was the hardest part for me
                                                                                         #I am not sure if there is a shorter way to write this code
                                                                                         #I get the right output and I got to practice formatting which was cool
your_String = input("Please enter a sentance:")            #the sample problem on the homework sheet shows getting user input of the string
count_letters(your_String)