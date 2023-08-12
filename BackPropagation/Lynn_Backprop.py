#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 09:26:24 2022

@author: lynntao
"""
import numpy as np
import sys
import math
import random
import time


def sigmoid(num):
    return 1/(1+math.exp(num*-1))


def d_sigmoid(num):
    return sigmoid(num) * (1- sigmoid(num))
    

def p_net(A, x, w_list, b_list):
    sig = np.vectorize(A)
    a_l = x
    for i in range(1, len(w_list)):
        dotL = a_l@w_list[i] + b_list[i]
        # print(dotL)
        a_l = sig(dotL)
        # print(a_l)
    
    return a_l

# CHALLENGE 1 - BACKPROP
def backprop(A, B, x, y, w_list, b_list, lamba):
    sig = np.vectorize(A)
    dsig = np.vectorize(B)
    
    dot = [0]
    a = [x]
    aL = x
    for i in range(1, len(w_list)):
        dotL = aL@w_list[i] + b_list[i]
        aL = sig(dotL)
        dot.append(dotL)
        a.append(aL)
        
    delta_n = dsig(dotL) * (y-aL)
    delta_l = delta_n
    
    deltas = [0, delta_l]
    for i in range(len(w_list)-2, 0, -1):
        delta_l = dsig(dot[i]) * (delta_l@(w_list[i+1].transpose()))
        deltas.insert(1, delta_l)
        
    for i in range(1, len(w_list)):
        b_list[i] = b_list[i] + lamba * deltas[i]
        w_list[i] =  w_list[i] + lamba * ((a[i-1].transpose())@deltas[i])
    
    return [w_list, b_list]


def sum_backprop(A, B, train, w_list, b_list, lamba):
    sig = np.vectorize(A)
    dsig = np.vectorize(B)
    
    for i in range(0, 5000):
        for [x, y] in train: 
            dot = [0]
            a = [x]
            aL = x
            for i in range(1, len(w_list)):
                dotL = aL@w_list[i] + b_list[i]
                aL = sig(dotL)
                dot.append(dotL)
                a.append(aL)
                
            print("Output Perceptron:" + str(aL))
            mag = np.linalg.norm((y-aL))
            print("Error:" + str(.5*(mag**2)))
            print()
            
            delta_n = dsig(dotL) * (y-aL)
            delta_l = delta_n
            
            deltas = [0, delta_l]
            for i in range(len(w_list)-2, 0, -1):
                delta_l = dsig(dot[i]) * (delta_l@(w_list[i+1].transpose()))
                deltas.insert(1, delta_l)
                
            for i in range(1, len(w_list)):
                b_list[i] = b_list[i] + lamba * deltas[i]
                w_list[i] =  w_list[i] + lamba * ((a[i-1].transpose())@deltas[i])

    return [w_list, b_list]


def circle_backprop(A, B, train, w_list, b_list, lamba):
    sig = np.vectorize(A)
    dsig = np.vectorize(B)
    
    for i in range(0, 50):
        print("Epoch: " + str(i))
        for [x, y] in train: 
            dot = [0]
            a = [x]
            aL = x
            for i in range(1, len(w_list)):
                dotL = aL@w_list[i] + b_list[i]
                aL = sig(dotL)
                dot.append(dotL)
                a.append(aL)
            
            delta_n = dsig(dotL) * (y-aL)
            delta_l = delta_n
            
            deltas = [0, delta_l]
            for i in range(len(w_list)-2, 0, -1):
                delta_l = dsig(dot[i]) * (delta_l@(w_list[i+1].transpose()))
                deltas.insert(1, delta_l)
                
            for i in range(1, len(w_list)):
                b_list[i] = b_list[i] + lamba * deltas[i]
                w_list[i] =  w_list[i] + lamba * ((a[i-1].transpose())@deltas[i])
            
        count = 0
        for item in train: 
            result = p_net(A, item[0], w_list, b_list)
            result = round(result[0][0], 0)
            if result != item[1]:
                count+=1
        print("Misclassified Points: " + str(count))
        print()   
        
    return [w_list, b_list]



# CHALLENGE 1 - BACKPROP
# SETUP
# x = np.array([[2, 3]])
# y = np.array([[.8, 1]])
# lamba = 0.1
# weight_list = [None, np.array([[1, -.5], [1, .5]]), np.array([[1, 2], [-1, -2]])]
# bias_list = [None, np.array([[1, -1]]), np.array([[-.5, .5]])]
# NEW WEIGHTS AND BIASES AFTER 1 BACKPROP
# weight_list = [None, np.array([[ 1.0000519 , -0.50494448], [1.00007784,  0.49258328]]), np.array([[ 1.00671011,  2.00189194], [-0.99746038, -1.99928395]])]
# bias_list = [None, np.array([[ 1.00002595, -1.00247224]]), np.array([[-0.49327326,  0.50189663]])]
# final = backprop(sigmoid, d_sigmoid, x, y, weight_list, bias_list, lamba)
# print(final[0])
# print(final[1])
# CHECK ERROR VALUE
# final = p_net(sigmoid, x, weight_list, bias_list)
# print(final)
# mag = np.linalg.norm((y-final))
# print(.5*(mag**2))

# CHALLENGE 2 - SUM
arg = sys.argv[1:]
if arg[0] == "S":
    # TRAINING
    print("TRAINING!")
    start = time.perf_counter()
    lamba = .7
    train = [[np.array([[0, 0]]), np.array([[0, 0]])], 
              [np.array([[0, 1]]), np.array([[0, 1]])],
              [np.array([[1, 0]]), np.array([[0, 1]])],
              [np.array([[1, 1]]), np.array([[1, 0]])],
              ]
    weight_list = [None, np.array([[random.random()*2-1, random.random()*2-1], [random.random()*2-1, random.random()*2-1]]), np.array([[random.random()*2-1, random.random()*2-1], [random.random()*2-1, random.random()*2-1]])]
    bias_list = [None, np.array([[random.random()*2-1, random.random()*2-1]]), np.array([[random.random()*2-1, random.random()*2-1]])]
    final = sum_backprop(sigmoid, d_sigmoid, train, weight_list, bias_list, lamba)
    end = time.perf_counter()
    print("Time:" + str(end-start))
    print()
    # TESTING
    print("TESTING!")
    # CHANGE BELOW X TO TEST VALUES
    x = [1, 0]
    print("INPUT: " + str(x))
    result = p_net(sigmoid, x, final[0], final[1])
    print([round(result[0][0], 0), round(result[0][1], 0)])

# CHALLENGE 3 - CIRCLE
    # TRAINING
arg = sys.argv[1:]
if arg[0] == "C":
    print("TRAINING!")
    lamba = .3
    start = time.perf_counter()
    weight_list = [None, np.array([[random.random()*2-1, random.random()*2-1, random.random()*2-1, random.random()*2-1], [random.random()*2-1, random.random()*2-1, random.random()*2-1, random.random()*2-1]]), np.array([[random.random()*2-1], [random.random()*2-1], [random.random()*2-1], [random.random()*2-1]])]
    bias_list = [None, np.array([[random.random()*2-1, random.random()*2-1, random.random()*2-1, random.random()*2-1]]), np.array([[random.random()*2-1]])]
    points = []
    with open("/Users/lynntao/Downloads/AI/Backprop/10000_pairs.txt", encoding='utf-8-sig') as f:
        f = f.read().split("\n")
        for i in range(0,len(f)):
            point = f[i].split()
            point = [float(x) for x in point]
            if point[0]**2 + point[1]**2 < 1:
                points.append([np.array([point]), 1])
            else:
                points.append([np.array([point]), 0]) 
    final = circle_backprop(sigmoid, d_sigmoid, points, weight_list, bias_list, lamba)
    end = time.perf_counter()
    print("Time:" + str(end-start))
