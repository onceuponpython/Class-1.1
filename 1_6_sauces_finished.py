# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 08:28:03 2018

@author: Owner
"""
# The below is a bucket holding the name of two sauces (in the form of text).
sauces=["Alfredo", "tomato"]
# The below line adds pesto to the sauces bucket.
sauces.append("pesto")
# The below line of code asks Pythanna to print out the items in the saucses bucket.
print(sauces)
sauces.remove("Alfredo")
print(sauces)
# Write a line of code to add marinara to the sauces bucket.
sauces.append("marinara")

# Write a line of code to add another tomato to the sauces bucket.
sauces.append("tomato")

# Write a line of code to print all of the items now in the sauces bucket.
print(sauces)

# Write a line of code to delete the first tomato item from the sauces bucket.
sauces.remove("tomato")

# Write a line of code to print "At the end of the program, the sauces bucket has:" and then the list of items in the bucket without manually entering the items yourself.
print("At the end of the program, the sauces bucket has: ", sauces)
# Write a line of code to print out the number of items in the sauces bucket.
print(len(sauces))


