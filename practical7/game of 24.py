# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:06:54 2019

@author: Jessi
"""
from fractions import Fraction
n=input("please input the number to compute 24(use ',' to divide them):" )
x=n.split(',')#delete , and add number to x
yl=[int(i) for i in x]
y=list(map(int,x))
for i in yl:
    if i in range(1,24):
        i==i
    else:
        break
        print("the number should range from 1 to 24") #judge whether the input is suitable for requests


count = 0 #to store the recursion times

#n is len(yl) 
def dfs(n):
    global count
    count = count +1
    
    if n == 1:
        if(float(yl[0])==24):
            return 1#to judge whether the final calculating result is equal to 24
        else:
            return 0
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):#eg.when i=0
            x = yl[i]#x store the first element 
            y = yl[j]#from the rest, eg.y store the second element
            yl[j] = yl[n-1]#replace the second with the value of the final element
            
            yl[i] = x+y
            if(dfs(n-1)==1):#it call the function again, and this time the final element is reduced because of the reduced length,which prevent the repetitiness
                return 1#at every step it have 4 operation(+-*/),if the operators choosen can not achieve the goal it goes back to the former step and rechoose an operator,and so on
            
            yl[i] = x-y
            if(dfs(n-1)==1):
                return 1  
            
            yl[i] = y-x
            if(dfs(n-1)==1): 
                return 1 
            
            yl[i] = x*y
            if(dfs(n-1)==1): 
                return 1  
            
            if x>=1:#the number divisor can not be 0
                yl[i] = Fraction(y,x)
                if(dfs(n-1)==1): 
                    return 1                 #floats are not precise
                
            if y>=1:
                yl[i] = Fraction(x,y)
                if(dfs(n-1)==1): 
                    return 1 
            #Backtracking  
            yl[i] = x
            yl[j] = y#if the number you choose can not succeed, get back and change
    return 0 

if (dfs(len(yl))): 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)
# print and output the result
        
        
        
        
#reference from Chen Xin
"""
#to choose 2 numbers from the array and choose (+-*/)
#do the binary calculation of the two numbers
#Change list: remove the two Numbers in this array and put the calculatuon result into the list
#the new list will also undergo the former procedure 
n=input("please input the number to compute 24(use ',' to divide them):" )
a=n.split(',')#
b=[int(i) for i in a]
#b=list(map(int,a))
#we need to judge whether the number we print in is qualified, ranged in(1,24)
for i in b:
    if i in range(1,24):
        i==i
    else:
        break
        print("the number should range from 1 to 24") 
import itertools
c=b[:] 
recursion=0
def function(c):#change the function
    l=itertools.combinations(c,2)
    #to obtain all the combinations types of the chosen number
    c=b[:] 
    s=list(l)
    for elem in s:#the number in one combinition
        d=[elem[0]+elem[1],elem[0]-elem[1],elem[0]*elem[1],elem[0]/elem[1],elem[1]-elem[0],elem[1]/elem[0]]
        print ('the deposition with the chosen two number',d)
        c.remove(elem[0])
        c.remove(elem[1])
        s.remove(elem)
    #we need to pay attention to the a=0
        for i in range(len(d)):
            c.append(d[i])
        if len(c)==1:hen there is only one number left, use a large loop to determine if the last value is equal to 24
           print(c[0]==24)
           recursion+=1
    function(c)
function(c)    

print('recursion=',recursion)

"""   
    
    
             
        
       
            
            
            
    

              
                  
    
       
         
    
    
    


    
    
    
     
    




        
    
    

