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
population[99,99]=1
max=0
n=1000
m=n-1
for rate in range(0,11):
    list2=[]
    list2= np.array(list2)
    population=np.zeros((100,100))
    population[99,99]=1
    rate_real=rate*10
    for r in range(0,rate_real):
      population[r]=[2]*100
    else:
      for i in range(1,n):
            pop=population
            pop=[x for x in pop.flatten()] 
            population_1=Counter(pop)
            num1=int(population_1[1])    
            possible=num1/10000
            b=beta*possible
            se=0
            for sep in population:
                for p in range(0, len(sep)): 
                    if population[se,p]==0:
                        population[se,p]=np.random.choice(a=2,size=1,p=[1-b,b])[0]
                    elif population[se,p]==1:
                        population[se,p]=np.random.choice(a=3,size=1,p=[0,1-gamma,gamma])[0]
                se=se+1
            if max<int(num1):
                max=int(num1)
            list2= np.array(list2)
            list2=list2.tolist()
            list2.append(num1)
    t = np.arange(0,m,1)
    list2= np.array(list2)
    plt.plot(t,list2[t],label=str(rate*10)+"%")
plt.legend()
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.show()
