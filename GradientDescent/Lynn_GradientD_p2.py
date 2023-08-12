#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:08:24 2022

@author: lynntao
"""
import numpy as np
import sys
import math

# GRADIENT PART 2
def make_funct_A(arr, grad):
    def functA(lamba):
        loc = grad*lamba 
        loc = arr - loc
        return 4*loc[0]**2 - 3*loc[0]*loc[1] + 2*loc[1]**2 + 24*loc[0] - 20*loc[1]
    return functA

def make_funct_B(arr, grad):
    def functB(lamba):
        loc = grad*lamba 
        loc = arr - loc
        return (1-loc[1])**2 + (loc[0]-loc[1]**2)**2
    return functB

def one_d_minimize(f, left, right, tolerance):
    if right - left < tolerance:
        return (right+left)/2
    one_third = left + (right-left)/3
    two_third = right - (right-left)/3
    if f(one_third) > f(two_third):
        return one_d_minimize(f, one_third, right, tolerance)
    else:
        return one_d_minimize(f, left, two_third, tolerance)
    
def f(x):
    return math.sin(x) + math.sin(3*x) + math.sin(4*x)


arg = sys.argv[1:]
arr = np.array([0, 0])
if arg[0] == "A":
    grad = np.array([24, -20])
    while np.linalg.norm(grad) > 10**(-8):
        fA = make_funct_A(arr, grad) 
        # LINE OPTIMIZATION
        lamba = one_d_minimize(fA, 0, 1, 10**(-8))
        arr = arr - lamba * grad
        grad = np.array([8*arr[0] - 3*arr[1] + 24, 4*arr[1] - 20 - 3*arr[0]])
        print("Location:" + str(arr))
        print("Gradient Vector:" + str(grad))
    print("\nFinal Location" + str(arr))
if arg[0] == "B":
    grad = np.array([0, -2])
    while np.linalg.norm(grad) > 10**(-8):
        fB = make_funct_B(arr, grad) 
        # LINE OPTIMIZATION
        lamba = one_d_minimize(fB, 0, 1, 10**(-8))
        arr = arr - lamba * grad
        grad = np.array([2*(arr[0] - arr[1]**2), 2*(-2*arr[0]*arr[1] + 2*arr[1]**3 + arr[1] - 1)])
        print("Location:" + str(arr))
        print("Gradient Vector:" + str(grad))
    print("\nFinal Location" + str(arr))


# print(one_d_minimize(f, -1, 0, 10**(-8)))
