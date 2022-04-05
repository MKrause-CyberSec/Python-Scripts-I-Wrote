'''Develop a recursive function called is_palindrome that takes a string as a parameter and returns
True if the string is a palindrome, False otherwise. Remember that a string is a palindrome if it
is spelled the same both forward and backward.  No global variables are used in the function.
Function parameters must be used.'''

def string_transform(string):              #function to simplify the string into only lowercase alphabetical characters
    alpha = []                             #setting the accumulator
    for char in(string):                   #checking all the characters in the string to see if they are alphabetical
        if char.isalpha():
            alpha.append(char)             #if the character is alphabetical appending it to the list alpha
    alpha = "".join(alpha)                 #getting rid of spaces and , and setting all the characters to lower case
    alpha = alpha.lower()

    is_palindrome(alpha)                   #calling the is_palindrome function with the list of characters

def is_palindrome(string):
    if len(string) <= 1:                   #the base case to end recursion
      print(True)                          #if the positions are the same down to the last 1 the function returns True
    elif string[0] == string[-1]:          #if the first and last position are the same the fuction repeats
        is_palindrome(string[1:len(string) -1])   #moving the position in by 1 and checking until it is lest than or equal to 1
    else:
      print(False)                         #if the two positions are not the same the function will print False





string_transform("Live not on evil!")
