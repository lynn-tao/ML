#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:35:51 2022

@author: lynntao
"""
import csv
import math
import random
import numpy as np
from tqdm import tqdm

# READ FILE
file = open('mnist_train_full.csv')
csvreader = csv.reader(file)
train = []
for row in csvreader:
    pi = [int(x)/255 for x in row[1:]]
    pixel = np.array([pi])
    label = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    label[0][int(row[0])] = 1
    train.append([pixel, label])
file.close()
# print(train)

def sigmoid(num):
    return 1/(1+math.exp(num*-1))

def d_sigmoid(num):
    return sigmoid(num) * (1- sigmoid(num))

def create_wb(architecture):
    h1 = architecture[0]
    h2 = architecture[1]
    h3 = architecture[2]
    h4 = architecture[3]
    wlist = []
    blist = []
    
    w1 = 2*np.random.rand(h1, h2) - 1
    b1 = 2*np.random.rand(1, h2)- 1
    w2 = 2*np.random.rand(h2, h3)- 1
    b2 = 2*np.random.rand(1, h3)- 1
    w3 = 2*np.random.rand(h3, h4)- 1
    b3 = 2*np.random.rand(1, h4)- 1

    wlist = [w1, w2, w3]
    blist = [b1, b2, b3]
    return [wlist, blist]
    

def p_net(A, x, w_list, b_list):
    sig = np.vectorize(A)
    a_l = x
    for i in range(1, len(w_list)):
        dotL = a_l@w_list[i] + b_list[i]
        a_l = sig(dotL)    
    return a_l


def circle_backprop(A, B, train, w_list, b_list, lamba):
    sig = np.vectorize(A)
    dsig = np.vectorize(B)
    
    for i in tqdm(range(0, 5)):
        # print("Epoch: " + str(i))
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
            
            temp = dsig(dotL)
            temp2 = y-aL
            delta_n = temp * (temp2)
            delta_l = delta_n
            
            deltas = [0, delta_l]
            for i in range(len(w_list)-2, 0, -1):
                delta_l = dsig(dot[i]) * (delta_l@(w_list[i+1].transpose()))
                deltas.insert(1, delta_l)
                
            for i in range(1, len(w_list)):
                b_list[i] = b_list[i] + lamba * deltas[i]
                w_list[i] =  w_list[i] + lamba * ((a[i-1].transpose())@deltas[i])

    return [w_list, b_list]


lamba = 0.07
wb = create_wb([784, 300, 100, 10])
w_list = [0]
w_list = w_list + wb[0]
b_list = [0]
b_list = b_list + wb[1]
final = circle_backprop(sigmoid, d_sigmoid, train, w_list, b_list, lamba)
w_list = final[0]
b_list = final[1]

# CHECK TRAINING CLASSIFICATION
# count = 0
# for item in train: 
#     result = p_net(sigmoid, item[0], w_list, b_list)
#     if result.argmax() != item[1].argmax():
#         count+=1
# print("Misclassified Points: " + str(count))
# print()  

# CHECK TESTING CLASSIFICATION
file = open('mnist_test.csv')
csvreader = csv.reader(file)
test = []
for row in csvreader:
    pi = [int(x)/255 for x in row[1:]]
    pixel = np.array([pi])
    label = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    label[0][int(row[0])] = 1
    test.append([pixel, label])
file.close()

count = 0
for item in test: 
    result = p_net(sigmoid, item[0], w_list, b_list)
    if result.argmax() != item[1].argmax():
        count+=1
print("Misclassified Points: " + str(count))
print()  

