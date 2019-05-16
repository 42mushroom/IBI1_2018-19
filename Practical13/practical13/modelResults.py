# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:34:37 2019

@author: 30389
"""

import pandas as pd
import numpy as np
df=pd.read_csv('modelResults.csv',header=None,sep=' ')
se=0
name=df[0:1] 
name=name.values
name=name[0][0]
name=name.split(",")
number_index=df.shape[0]
result=df[1:number_index]
result_fin=np.array([])
result_1=result.values[::][::]
for result_index in result_1:
    result_1[se]=.toint()　
    se=se+1
print(result_1)
