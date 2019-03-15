# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:16:42 2018

@author: Owner
"""

big_box=[]
picking_bucket=["A", "T", "MR", "MR", "MB", "GP", "P", "MR", "A", "T", "MB", "GP", "MR", "GP", "P", "P", "T", "A", "MB", "MR", "MR"]
veg_list=["MR", "GP", "T"]
fish_list=["A"]
meat_list=["MB", "P"]
veg_bucket=[]
fish_bucket=[]
meat_bucket=[]
#For loop begins below.
for topping in picking_bucket:
    if topping in veg_list:
        veg_bucket.append(topping)
    if topping in fish_list:
        fish_bucket.append(topping)
    if topping in meat_list:
        meat_bucket.append(topping)
#Below is the first line of code after the for loop.
big_box.append(veg_bucket)
big_box.append(fish_bucket)
big_box.append(meat_bucket)
print("veg_bucket")
print(veg_bucket)
print("fish_bucket")
print(fish_bucket)
print("meat_bucket")
print(meat_bucket)
print("big_box")
print(big_box)
print("The vegetable bucket has the following number of items: ", str(len(veg_bucket)))
print("The meat bucket has the following number of items: ", str(len(meat_bucket)))
print("The fish bucket has the following number of items: ", str(len(fish_bucket)))