#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:49:08 2020

@author: sahanaasokan
"""
a = "the fox jumps over the lazy dog"
a=a[::-1]
print(a)


#Check if its a Palindrome
import string
def isPalindrome(s):
    s=s.lower()    
    s=s.replace(" ","")
    return s == s[::-1]


string_1="Racecar"
string_2="bitchead"

print(isPalindrome(string_1))
print(isPalindrome(string_2))
  

#Check if String has unique characters
#Set"
#a set returns the unique elements of the string
s1= "unique"
x=set(s1)

s2= "bear"

def isUnique(u):
   return len(u) == len(set(u))

print(isUnique(s1))
print(isUnique(s2))



#FizzBuzz
N=15
for i in range(1, N+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")  
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)
        
#kth Largest element in an array unsorted array
import numpy as np
arr=np.array([1,2,3,4,5])
max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i] > max:
        max=arr[i]
print(max)


arr=np.array([1,2,3,4,5])
max=arr[0]
n=len(arr)

#Find the min in the array
for i in range(1,n):
    if arr[i] < max:
        max=arr[i]
print(max)



#Fibonnaci sequence
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        

print(fib(12)) 



 
#Dict, Key Value


#Sets,Dict,Lists, Tuples

Li=["hoe","ya","lol"]
Tu=("ya","we","kaka")
set1=set(["hoe","ya","lol"])
dict1={1:'butt',2:'kaka',3:'word'}















