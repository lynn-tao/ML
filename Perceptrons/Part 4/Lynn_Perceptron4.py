#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 08:32:56 2022

@author: lynntao
"""
import numpy as np
import math
import random
import sys
import ast

def perceptron(A, w, b, x):
    numsum = 0 
    for i in range(0, len(w)):
        numsum += w[i] * int(x[i])
    n = numsum + b
    a = A(n)
    return a
    

def step(num):
    if num > 0:
        return 1
    else:
        return 0

def sigmoid(num):
    return 1/(1+math.exp(num*-1))


def p_net(A, x, w_list, b_list):
    # print(b_list[2])
    new_f = np.vectorize(A)
    a_l = x
    for i in range(1, len(w_list)):
        one = a_l@w_list[i]
        two = b_list[i]
        three = one+two
        a_l = new_f(three)
    
    return a_l

# RUN CODE 
arg = sys.argv[1:]
# CHALLENGE 1 - NUMPY XOR HAPPENS HERE
if len(arg) == 1:
    inputs = ast.literal_eval(arg[0]) 
    inputs = list(inputs)
    weight_list = [None, np.array([[2, -2], [2, -2]]), np.array([[2], [2]])]
    bias_list = [None, np.array([[-1, 3]]), np.array([[-3]])]
    print(p_net(step, inputs, weight_list, bias_list)[0][0])

# CHALLENGE 2 - THE DIAMOND
if len(arg) == 2:
    x = float(arg[0])
    y = float(arg[1])
    weight_list = [None, np.array([[1, -1, -1, 1], [-1, -1, 1, 1]]), np.array([[1], [1], [1], [1]])]
    bias_list = [None, np.array([[1, 1, 1, 1]]), np.array([[-3.5]])]
    print(p_net(step, [x, y], weight_list, bias_list)[0][0])

# CHALLENGE 3 - THE SIGMOID FUNCTION CIRCLE
if len(arg) == 0:
    points = []
    for i in range(0, 500):
        x = random.random()*2-1
        y = random.random()*2-1
        points.append([x, y]) 
        
    # BEST NETWORK ==> Accuracy: .832 Max
    weight_list = [None, np.array([[1, -1, -1, 1], [-1, -1, 1, 1]]), np.array([[1], [1], [1], [1]])]
    bias_list = [None, np.array([[-10.1, -10.1, -10.1, -10.1]]), np.array([[.3]])]
      
    correct = 0  
    for item in points: 
            result = p_net(sigmoid, item, weight_list, bias_list)[0][0]
            if round(result, 0) == 1 and (item[0]**2 + item[1]**2) < 1:
                correct += 1
            elif round(result, 0) == 0 and (item[0]**2 + item[1]**2) >= 1:
                correct+= 1
            else:
                print(item)
        
    print("Accuracy: " + str(correct/500))

# TESTING FOR BEST NETWORK   
# weight_list = [None, np.array([[1, -1, -1, 1], [-1, -1, 1, 1]]), np.array([[1], [1], [1], [1]])]
# bias_list = [None, np.array([[-10, -10, -10, -10]]), np.array([[.3]])]

# for i in range(0, 100):
#     bias_list[2] = (bias_list[2] + .1)
#     # print(bias_list[2])
#     correct = 0
#     for item in points: 
#         result = p_net(sigmoid, item, weight_list, bias_list)[0][0]
#         # print(round(result, 0))
#         # print(result, 0)
#         if round(result, 0) == 1 and (item[0]**2 + item[1]**2) < 1:
#             correct += 1
#         elif round(result, 0) == 0 and (item[0]**2 + item[1]**2) >= 1:
#             correct+= 1 
#     print("Accuracy: " + str(correct/500))