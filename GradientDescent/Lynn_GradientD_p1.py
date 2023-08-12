#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:35:45 2022

@author: lynntao
"""
import numpy as np
import sys

# GRADIENT PART 1
arr = np.array([0, 0])
lamba = .01
arg = sys.argv[1:]
if arg[0] == "A":
    grad = [24, -20]
    while np.linalg.norm(grad) > 10**(-8):
        grad = np.array([8*arr[0] - 3*arr[1] + 24, 4*arr[1] - 20 - 3*arr[0]])
        arr = arr - lamba * grad
        print("Location:" + str(arr))
        print("Gradient Vector:" + str(grad))
    print("\nFinal Location" + str(arr))
if arg[0] == "B":
    grad = [0, -2]
    while np.linalg.norm(grad) > 10**(-8):
        grad = np.array([2*(arr[0] - arr[1]**2), 2*(-2*arr[0]*arr[1] + 2*arr[1]**3 + arr[1] - 1)])
        arr = arr - lamba * grad
        print("Location:" + str(arr))
        print("Gradient Vector:" + str(grad))
    print("\nFinal Location" + str(arr))

# PART 2
