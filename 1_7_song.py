# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:24:25 2019

@author: Owner
"""

names=[]
# asks the User's Name
x=input("Please give me your first name. ")
y=input("Please give me your middle name or make one up if you don't have one. ")
z=input("Please give me your last name. ")
# adds the three names given to the empty bucket we named names in the first line of code
names.append(x)
names.append(y)
names.append(z)
print("I just made up a song with your names in it. Hope you like it!")
# for loop to build the song
for name_given in names:
    print("Hanna, Hanna-" + name_given + "-banna")
    print("Banana-fana fo-" + name_given + "-fanna")
    print("Fee-fi-mo-" + name_given + "-manna")
    print("Hanna!")
    print("--------------------")
