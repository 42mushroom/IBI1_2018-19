# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:57:07 2019

@author: 30389
"""
s="the quick brown fox jumps over a lazy dog"
print("give me a string of words: "+ s)
s=s[::-1]
l=s.split(" ")
l.sort(reverse=True)
print(l)