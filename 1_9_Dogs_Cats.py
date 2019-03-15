# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:16:42 2018

@author: Owner
"""


group=["Meow", "Kitten", "Dog", "Cat", "Puppy", "Kitty", "K9"]
cat_list=["Meow", "Kitten", "Cat", "Kitty"]
dog_list=["Dog", "Puppy", "K9"]
cat_team=[]
dog_team=[]

#For loop begins below.
for student in group:
    if student in cat_list:
        cat_team.append(student)
    if student in dog_list:
        dog_team.append(student)
print("The members on the cat team are: ", cat_team)
print("The members on the dog team are: ", dog_team)

print("The cat team has the following number of members: ", str(len(cat_team)))
print("The dog team has the following number of members: ", str(len(dog_team)))