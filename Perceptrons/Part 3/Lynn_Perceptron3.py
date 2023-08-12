#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 14:32:18 2022

@author: lynntao
"""
import ast
import sys

def truth_table(bits, n):
    boolean = dict()
    funct = bin(n)[2:]
    
    entries = 2 ** bits
    front0 = entries-len(funct)
    for i in range(0, front0):
        funct = "0" + funct

    for i in range(entries-1, -1, -1):
        bins = bin(i)[2:]
        tup_bin = tuple()
        while len(bins) < bits:
            bins = "0" + bins
        for item in bins:
            tup_bin = tup_bin + (item,)  
        boolean[tup_bin] = int(funct[entries-i-1])
    
    return boolean
    

def pretty_print_tt(table):
    print("Inputs    |  Output")
    for item in table.keys():
        output = ""
        for obj in item:
            output += str(obj) + "   "
        output += "   " + str(table[item])
        print(output)
    
    
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


def check(n, w, b):
    table = truth_table(len(w), n)
    # pretty_print_tt(table)
    correct = 0
    for item in table.keys():
        if perceptron(step, w, b, item) == table[item]:
            correct += 1
    return correct/len(table)
    

def train(truth_table, lambda_rate):
    lambda_rate = 1
    b = 0
    w = []
    length = len(next(iter(truth_table)))
    for i in range(0, length):
        w.append(0)
    for i in range(0, 100):
        for item in truth_table.keys():
            f_star = perceptron(step, w, b, item)
            for i in range(0, len(w)):
                error = (truth_table[item] - f_star) * lambda_rate * int(item[i])
                w[i] = w[i] + error
            b = b + (truth_table[item] - f_star) * lambda_rate
    return [w, b]
    

def verify_training(truth_table, w, b):
    num = ""
    for item in truth_table.keys():
        num += str(truth_table[item])
    n = int(num, 2)
    accuracy = check(n, w, b)
    return accuracy
    

# PART 3 XOR CODE
def xor(input1, input2):
    w3 = [2,2]
    b3 = -1
    w4 = [-2,-2]
    b4 = +3
    w5 = [2,2]
    b5 = -3
    x1 = perceptron(step, w3, b3, (input1, input2))
    x2 = perceptron(step, w4, b4, (input1, input2))
    x = (x1, x2)
    
    output = perceptron(step, w5, b5, x)
    return output
    
    
# PART 3 XOR CODE RUN
arg = sys.argv[1:]
inputs = ast.literal_eval(arg[0]) 
print(xor(inputs[0], inputs[1]))

