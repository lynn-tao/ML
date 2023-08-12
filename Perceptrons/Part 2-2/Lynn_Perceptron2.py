#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 11:26:09 2022

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
    

# PART 2 TESTING ALL TRUTH TABLES - UNCOMMENT THIS TO CHECK
# bits = 4
# correct = 0
# for i in range(0, 2**(2**bits)):
#     table = truth_table(bits, i)
#     pretty_print_tt(table)
#     [w, b] = train(table, 1)
#     verify = verify_training(table, w, b)
#     if verify == 1.0:
#         correct += 1
#     print(verify)
    
# print("There are " + str(2**(2**bits)) + " possible functions; " + str(correct) + " functions can be correctly modeled.")


# PART 2 TWO COMMAND INPUT LINE
arg = sys.argv[1:]
print(arg)
bits = int(arg[0])
n = int(arg[1])
table = truth_table(bits, n)
pretty_print_tt(table)
[w, b] = train(table, 1)
print("Weight and Bias Vector: " + str([w,b]))
print("Accuracy: " + str(verify_training(table, w, b)))

