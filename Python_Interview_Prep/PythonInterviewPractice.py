#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:45:56 2020

@author: sahanaasokan
"""

#What is the difference  between a list and a tuple
#Lists can be modified after they are created (Mutable)
#Tuples can NOT be modified after they are created.
#Lists are ordered. Ordered by creation date.
#Tuples have structure, and you may have different data types.
#Lists are slower than tuples


#String interpolation
name='Sahana'
age='12'
print("Hello my name is %s and I am %s years old" % (name,age))
print(f'Hello {name}')

      
      
      
# == vs is
#== checks equality, and is checks identity

a=[1,2,3]
b=a
c=[1,2,3]
print(a==b)
print(a is c)
#a and c do not have the same identity

#decorator
def f1():
    print('Called f1')
print(f1) 
#functions are also objects in python, they can be passed around


#Decorator allows adding extra functionality to an existing function
#You pass that existing function, as well as the extra code.

def logging(func):
    def log_function_called():
        print(f'{func} called.')
        func()
    return log_function_called()
'''
@logging
def my_name():
    print('Sahana') 
    @logging
def friends_name():
    print('Naruto')
    my_name()
    friends_name()
 '''   




'''
#range function
# range(stop)
for i in range(10):
    print(i)
    
#range(start and stop)
for i in range(4, 10):
    print(i)
    
#range(start stop and step)
for i in range(2,10,2):
    print(i)
    
list(range(2,10,2))   

'''

#Define a class with two attributes color and speed:

class Car :
    def __init__(self, color, speed):
        self.color = color
        self.speed ='100 mph'

# Difference between instance, class, static.


#map function
values = [1,2,3,4]
add_three = lambda x:(x+3)
print(list(map(add_three,values)))

#reduce function iterating amongst each other, so there are two inputs x and y
from functools import reduce
data = [1,2,3,4]
multiplier = lambda x,y:(x*y)
print(reduce(multiplier,data))
    

#filter function returns what you want it to filter out
data1=[1,4,5,6,2]
function = lambda x:(x%2 == 0)
print(list(filter(function,data1)))


#How do we reverse a list
li=['3','4','6','1']
print(li)
li.reverse()
print(li)

#string multiplication
x= 'cat'* 3
print(x)


#list multiplication
x_1=[1,2,3]*2
print(x_1)

#What does self refer to in a class.
#Self refers to the instance of the class.
# It is how we give the methods access/update the object they belong too

class Shirt:
    def __init__(self,color):
        self.color = color
s=Shirt('Yellow')
print(s.color)

    
#How can you concatenate lists in python
a=[1,2]
b=[3,4,5]
print(a+b)


#What is the difference between list and arrays
# Lists exist in the standard library
# Arrays are defined by Numpy

#Lists can hold diffferent types of data, arrays are homogenous.
#arithmetics on lists adds/removes elements from the list
#arithmetic on arrays functions per linear algebra

#How do Concatenate two arrays
import numpy as np
array_1=np.array([1,2,3])
array_2=np.array([3,2,7])
tik=array_1+array_2
print(tik)
array_final=np.concatenate((array_1,array_2))

# Mutable vs Immutable Objects
#Immutable objects means that it cant be modified after created
#Examples: int, float, bool, string and tuple

#Mutable Objects can be changes
#Examples are list, dict, set


#How would you round a number to 3 decimal places
s=5.3823721
round(s,3)

#How do you slice a list
#list[start:stop:step]
kaka=[1,3,5,4,2,7,8,6,4]
print(kaka[0:10:2])


#What is pickling
#serializing and unserializing objects in python.


#Dict is a python datatype, json is a string that follows a specific format.

#ORMS: Object Relational Mapping: SQLAlchemy, Flask. Django

#How do any and all work?
#Any returns true if any element is true
#All only returns true if all the elements re true

Yeah= ['false','false','false']
no=['true','true','true']
print(any(no))
print(all(no))

#Looking up a value in a dict is faster cause it uses hashtables

#A module is a collection of files that can be imported
#A package is a directory of modules

'''import sklearn #module
from sklearn import cross_validation #package
'''

#How to increment and decrement an integer in Python


#How to return the binary of an integer
print(bin(5))

#How to remove duplicate elements from a list set()
example = [1,2,3,1,1,4,5,6,2,6]
yaya=list(set(example))
print(yaya)


#How to check if a value exists in a list
print('a' in ['b','c','d'])


#What is the difference between append and extend
#append adds value directly to a list
#extend adds values in another list to the list

boobie=[1,4,63,5,2]
kakatake=[5,2,6,7]
boobie.append(5)
print(boobie)
boobie.extend(kakatake)
print(boobie)


#How to take the absolute value of an integer
print(abs(-2))

#How to combine two lists into a list of tuples
lala=['a','b','c']
b=[1,2,3,4,5]
print([(k,v) for k,v in zip(lala,b)])

#How do you sort
d = {'c':3,'d':4,'b':2,'a':1}
print(sorted(d.items()))


#How does a class inherit from another class in python
#parent class
'''
class Car():
    def __init__(self):
        print('vroom')
    class Audi(Car):
        passaudi=Audi()
audi.dirve
         
'''


#How can you remove all whitespace from a string
yer = 'A string with    white space'
yer= yer.replace(' ','') 
print(yer)


#Enumerate?

#Pass Break Continue for for loops
#Convert the for loop into a list comprehension

#How to reverse an array

reverse=np.array([5,6,2,7,2])

print(reverse)
reverse=reverse[::-1]
print(reverse)

import random
lala=random.random


#List vs Set vs Tuple vs Dict






    