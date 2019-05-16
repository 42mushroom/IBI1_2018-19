# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:59:24 2019

@author: 30389
"""
DNA= input("please input a DNA sequence")
a=DNA.count("a",0,len(DNA))
t=DNA.count("t",0,len(DNA))
c=DNA.count("c",0,len(DNA))
g=DNA.count("g",0,len(DNA))
print("A:"+str(a)+" G:"+str(g)+" C:"+str(c)+" T:"+str(t))
from matplotlib import pyplot as plt
labels=['a','g','c','t']
sizes=[a,g,c,t]
patches,text1,text2=plt.pie(sizes,labels=labels,autopct='%1.2f%%')
plt.title("pie of the four DNA nucleotides")
plt.axis('equal')
plt.show()
