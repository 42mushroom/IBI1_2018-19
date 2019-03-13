# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:27:07 2019

@author: 30389
"""

import random
n=random.randint(1,8192) #set one random value
print("n="+str(n))
a=""#set the value for result
while n>0:
    p=n%2#find the remainder
    a=str(int (p))+a#put the reminder before the last result a
    n=(n-p)/2#culculate the next n for the next reminder
print("binary="+str(a))# print out the result



import random
n=random.randint(1,8192) #set one random value
k=n#record the initial n
b=""
i=0
while n>0:
    p=n%2#find the reminder
    if  p==1:
        b=b+"+2**"+str(i)#put the reminder before the last result
        i=i+1#record the numble of powers
        n=(n-p)/2#culculate the next n for the next reminder
    else:
        i=i+1
        n=(n-p)/2
    if n==0:#end this loop
        break
print(str(k)+"=0"+b)#print out the result
    
    
    