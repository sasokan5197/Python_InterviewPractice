#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:58:51 2020

@author: sahanaasokan
"""


#Serialization vs Unserialization
example_dict={1:'s',2:'a',3:'c'}
import pickle

pickle_output = open("pickle_file", "wb" )
pickle.dump(example_dict,pickle_output)
pickle_output.close()
loaded_object= pickle.load(pickle_output)
print(loaded_object)



#Ternary Operator
#One line if then statemet
k=10
b=5
k if k > b else k
