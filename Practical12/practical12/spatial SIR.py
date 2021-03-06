# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:01:03 2019

@author: 30389
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
population=np.zeros((100,100)) #set a 2 axis array to express the population
beta=0.3
gamma=0.05 #set the variables
outbreak=np.random.choice(range(100),2)
population [outbreak[0], outbreak[1]] = 1 #set a random patient
max=0
n=100 # set the number of circulation
m=n 
population_recent=population
for i in range(0,n):
        pop=population
        pop=[x for x in pop.flatten()] 
        population_1=Counter(pop)
        num1=int(population_1[1]) #count number of patients
        b=beta
        se=0
        population_recent = np.insert(population,100, values=[[0]*100], axis=0)
        population_recent = np.insert(population_recent,100, values=[[0]*101], axis=1)#prevent the se+1 and p+1 over the boundary of population
        if i==0 or i==10 or i==50:
            plt.figure(figsize = (6,4) , dpi =150)
            plt.imshow (population,cmap='viridis',interpolation='nearest')
            plt.savefig( "figure" + str(i), type="png")# gain the heatmap
        for sep in population:
            for p in range(0, len(sep)): 
                if population[se,p]==0 and se==0 and p==0 and (population_recent[se,p+1]==1 or population_recent[se+1,p]==1 or population_recent[se+1,p+1]==1):
                    population[se,p]=np.random.choice(a=2,size=1,p=[1-b,b])[0]
                elif population[se,p]==0 and se==0 and p>0 and ( population_recent[se,p-1]==1 or population_recent[se,p+1]==1 or population_recent[se+1,p-1]==1 or population_recent[se+1,p]==1 or population_recent[se+1,p+1]==1):
                    population[se,p]=np.random.choice(a=2,size=1,p=[1-b,b])[0]
                elif population[se,p]==0 and se>0 and p==0 and ( population_recent[se-1,p]==1 or population_recent[se-1,p+1]==1 or population_recent[se,p+1]==1 or population_recent[se+1,p]==1 or population_recent[se+1,p+1]==1):
                    population[se,p]=np.random.choice(a=2,size=1,p=[1-b,b])[0]
                elif population[se,p]==0 and se>0 and p>0 and (population_recent[se-1,p-1]==1 or population_recent[se-1,p]==1 or population_recent[se-1,p+1]==1 or population_recent[se,p-1]==1 or population_recent[se,p+1]==1 or population_recent[se+1,p-1]==1 or population_recent[se+1,p]==1 or population_recent[se+1,p+1]==1):
                    population[se,p]=np.random.choice(a=2,size=1,p=[1-b,b])[0]#the transformation of health to patient
                elif population[se,p]==1:
                     population[se,p]=np.random.choice(a=3,size=1,p=[0,1-gamma,gamma])[0]#the transformation of patient to recovery
            se=se+1
        if max<int(num1):
            max=int(num1)# gain the max of patient
        population_recent=population
max=str(max)
print(num1,"max="+max)
plt.figure(figsize = (6,4) , dpi =150)
plt.imshow (population,cmap='viridis',interpolation='nearest')
plt.savefig( "figure" + str(n), type="png")# gain the final heatmap

