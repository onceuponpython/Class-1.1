# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 07:20:32 2019

@author: Owner
"""

mushroom_weights=[12,2,6]
price=2
final_price=[]
for mushroom in mushroom_weights:
    mushroom_price=mushroom*price
    final_price.append(mushroom_price)
total=sum(final_price)
if total>30:
    print("You can buy a steak and a bag of bones.")
else:
    print("Better stick to tuan fish and dog food.")