#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:05:58 2020

@author: sahanaasokan
"""

def mydecorator(func):
    def lala():
        print('Inside of the decorator before calling the fucntion')
        func()
        print('Inside of the decorator after calling the function')

    return lala


@mydecorator
def printname():
    print('Sahana Asokan')
    
    
    
    
    
    