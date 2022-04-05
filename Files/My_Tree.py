'''] Please create your tree by customizing the following code. Explain in detail how the code works.
Do not state the obvious such as what each line of the code does.
The program will run from 80 down to its base case to form the first part of the tree making 30 degree turns as it subtracts 15.
It then turns left and works through the recursion call until it reaches the base case on the second branch.It runs through the
second recusion call as it backs up to form new branches until it goes back down to the bottom of the tree'''
import turtle

def tree(branchLen,t):
    if branchLen > 5:                  #the base case if the branchLen is over 5 the program will call itself
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-15,t)           #the program will go forward by the first parameter 80 and then turn right, it will call itself and subtract 15 and turn 30 until it is 5 or less
        if branchLen <= 20:            #I added an if statement to turn the last leg of the recursive pattern green because it is the leaf
            t.pensize(3)
            t.color("green")
        t.left(60)
        tree(branchLen-15,t)            #the second recursion call moves the turtle back down the branches to the base case to set up new branches
        t.right(30)
        t.backward(branchLen)
        if branchLen >= 15:
            t.pensize(2)
            t.color("brown")



def main():
    t = turtle.Turtle()                   #creates the turtle and sets its position for the recursive pattern
    myWin = turtle.Screen()
    t.speed(1)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(80,t)                             #parameters to be passed to the tree function the 80 parameter will
    myWin.exitonclick()                    #be the parameter that we subract from with every pass or branch

main()
