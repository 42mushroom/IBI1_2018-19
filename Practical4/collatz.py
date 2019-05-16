# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:36:57 2019

@author: 30389
"""
import random
n=random.randint(1,1000) #set one random value
print(n)#tell me the value
i=0#set a value for the loop time
collatzsequence=[]  
while n>1:#continue the loop until n==1
    collatzsequence.append(n) 
    if n%2==0:#if n mod 2 = 0
        n=n/2#calculate n/2 
        i=i+1#save the loop number
    else:
        n=3*n+1#calculate 3n+1
        i=i+1#save the loop number
    if n==1 :# end the loop when n=1
            break 
collatzsequence.append(n) 
print (collatzsequence,"i = " + str(i))#print out the time of loop

        