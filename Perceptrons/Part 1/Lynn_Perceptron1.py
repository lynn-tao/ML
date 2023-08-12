#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 14:21:27 2022

@author: lynntao
"""
import ast
import sys

x = "(1, 2, 3, 4, 5)"
t = ast.literal_eval(x) 
print(t, type(t))

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
    pretty_print_tt(table)
    correct = 0
    for item in table.keys():
        if perceptron(step, w, b, item) == table[item]:
            correct += 1
    return correct/len(table)
    

arg = sys.argv[1:]
print(arg)
n = int(arg[0])
tup = ast.literal_eval(arg[1]) 
bias = float(arg[2])

print(check(n, tup, bias))

# truth_table(2, 5)
# pretty_print_tt(truth_table(3, 128))
# print(perceptron(step, (1,1), -1.5, (1,0)))
# print(check(50101, (3, 2, 3, 1), -4))