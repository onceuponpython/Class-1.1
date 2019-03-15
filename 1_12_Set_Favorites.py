# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 20:16:32 2019

@author: Owner
"""

favorite={"yellow", "christmas", "dog"}
holiday=input("What is your favorite holiday? ")
color=input("What is your favorite color? ")
animal=input("What is your favorite animal? ")
user_fav=set()
holiday=holiday.lower()
color=color.lower()
animal=animal.lower()
user_fav.add(holiday)
user_fav.add(color)
user_fav.add(animal)
#print(user_fav)
match=favorite.intersection(user_fav)
print("MATCH")
print(match)
number_same=len(match)
if number_same == 1:
    print("You and I have: " + str(number_same) + " favorite that matches.")
if number_same > 1:
    print("You and I have: " + str(number_same) + " favorites that match.")
if number_same == 0:
    print("We don't have any favorites that match.")
my_different=favorite.difference(user_fav)
your_different=user_fav.difference(favorite)
print(your_different)
print(my_different)
number_diff=len(my_different)
if number_diff >0:
    print("Here's my favs that are not yours:")
    print(my_different)
    print("Your favs that are not mine: ")
    print(your_different)
    