# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:43:11 2019

@author: Owner
"""
import random as rnd

n=input("What is your name? ")
print("Hello", n)


random_pick=rnd.randrange(0,10)
#The below line of code is not executed because of the hash tag sign (also referred to as the numbered sign) is present before the line of code.
#print(str(random_pick))

# complete the below line of code by telling Pythanna that you will refer to the user's answer to the below question as the variable x.
x=input("Guess the number that I am thinking of which is between 1 and 10? Please enter that number. ")

# This line of code turns the user's answer from text to a number (specifically an integer).
y=int(x)

# The next two lines of code tell Pythanna that if the number she picked is equal to the number the user picked, she should print "You are correct! You win."
if random_pick==y:
    print("You are correct! You win.")


# The next two lines of code tell Pythanna that if the user guessed wrong, then she should print "Sorry, try again."  
if random_pick!=y:
    print("Sorry, try again.")
    
    ##Complete the below line of code by telling Pythanna to print "Please enter the number you think I have picked." Hint: all text should be enclosed in parantheses.
    a=input("Please enter the number you think I have picked." )
    ##The below line of code changes the user's answer from text to a number.
    z=int(a)
    ##The below two lines of code tell Pythanna that if the user's answer was equal to the number she picked print "You are correct! You win."
    if random_pick==z:
        print("You are correct! You win.")
    ##The below line of code tells Pythanna that if the number the user picked is not the same as the one she picked print "Sorry you lose."
    if random_pick!=z:
        print("Sorry, you lose.")
        ##Write a line of code by telling Pythanna to print "The number I was thinking of was:"
        print("The number I was thinking of was:")
        ##The below liine of code tells Pythanna to change the number she picked into text and then print the number as text.
        print(str(random_pick))




