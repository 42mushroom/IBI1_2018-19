# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:01:03 2019

@author: 30389
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
population=np.zeros((100,100))
beta=0.3
gamma=0.05
outbreak=np.random.choice(range(100),2)
population [outbreak[0], outbreak[1]] = 1
max=0
n=100
m=n-1
population_recent=population
for i in range(1,n):
        pop=population
        pop=[x for x in pop.flatten()] 
        population_1=Counter(pop)
        num1=int(population_1[1])
        num0=int(population_1[0])
        num2=int(population_1[2])       
        b=beta
        se=0
        population_recent = np.insert(population,100, values=[[0]*100], axis=0)
        population_recent = np.insert(population_recent,100, values=[[0]*101], axis=1)
        if i==1 or i==10 or i==50 or i==m:
            plt.figure(figsize = (6,4) , dpi =150)
            plt.imshow (population,cmap='viridis',interpolation='nearest')
        for sep in population:
            for p in range(0, len(sep)): 
                if population[se,p]==0 and se==0 and p==0 and (population_recent[se,p+1]==1 or population_recent[se+1,p]==1 or population_recent[se+1,p+1]==1):
                    population[se,p]=np.random.choice(a=2,size=1,p=[1-b,b])[0]
                elif population[se,p]==0 and se==0 and p>0 and ( population_recent[se,p-1]==1 or population_recent[se,p+1]==1 or population_recent[se+1,p-1]==1 or population_recent[se+1,p]==1 or population_recent[se+1,p+1]==1):
                    population[se,p]=np.random.choice(a=2,size=1,p=[1-b,b])[0]
                elif population[se,p]==0 and se>0 and p==0 and ( population_recent[se-1,p]==1 or population_recent[se-1,p+1]==1 or population_recent[se,p+1]==1 or population_recent[se+1,p]==1 or population_recent[se+1,p+1]==1):
                    population[se,p]=np.random.choice(a=2,size=1,p=[1-b,b])[0]
                elif population[se,p]==0 and se>0 and p>0 and (population_recent[se-1,p-1]==1 or population_recent[se-1,p]==1 or population_recent[se-1,p+1]==1 or population_recent[se,p-1]==1 or population_recent[se,p+1]==1 or population_recent[se+1,p-1]==1 or population_recent[se+1,p]==1 or population_recent[se+1,p+1]==1):
                    population[se,p]=np.random.choice(a=2,size=1,p=[1-b,b])[0]
                elif population[se,p]==1:
                     population[se,p]=np.random.choice(a=3,size=1,p=[0,1-gamma,gamma])[0]
            se=se+1
        if max<int(num1):
            max=int(num1)
        population_recent=population
print(num1,max)
plt.figure(figsize = (6,4) , dpi =150)
plt.imshow (population,cmap='viridis',interpolation='nearest')

