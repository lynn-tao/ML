#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:57:22 2022

@author: lynntao
"""

import csv
import math
import random

# READ FILE
file = open('star_data_training.csv')
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

# MAKE DATASET
star_type = dict()
dataset = []
color = []
spec = []
for star in rows:
    star_info = (math.log10(float(star[0])), math.log10(float(star[1])), math.log10(float(star[2])), float(star[3]), star[4], star[5], star[6])
    dataset.append(star_info)
    if star[5] not in color:
        color.append(star[5])
    if star[6] not in spec:
        spec.append(star[6])
    star_type[star_info] = star[4]

# print(dataset)
print("TRAINING STAGE")
print("\nThese are the attributes we are comparing: Star Color and Star Spectral")
print("\nStar Color:   " + str(color))
print("Star Spectral:   " + str(spec))

# FOR 1R CLASSIFICATION FOR COLOR

rcount = 0
ocount = 0
bwcount = 0
wcount = 0
wicount = 0
bcount = 0
ywcount = 0
ycount = 0
pyocount = 0
orcount = 0
pain_list = [rcount, ocount, bwcount, wcount, wicount, bcount, ywcount, ycount, pyocount, orcount]


raccuracy = [0, 0, 0, 0, 0, 0]
oaccuracy = [0, 0, 0, 0, 0, 0]
bwaccuracy = [0, 0, 0, 0, 0, 0]
waccuracy = [0, 0, 0, 0, 0, 0]
wiaccuracy = [0, 0, 0, 0, 0, 0]
baccuracy = [0, 0, 0, 0, 0, 0]
ywaccuracy = [0, 0, 0, 0, 0, 0]
yaccuracy = [0, 0, 0, 0, 0, 0]
pyoaccuracy = [0, 0, 0, 0, 0, 0]
oraccuracy = [0, 0, 0, 0, 0, 0]
final_list = [raccuracy, oaccuracy, bwaccuracy, waccuracy, wiaccuracy, baccuracy, ywaccuracy, yaccuracy, pyoaccuracy, oraccuracy]

cat = [0, 1, 2, 3, 4, 5]
for col in color:
    for star in dataset:
        if star[5] == col:
            if col == "Red":
                rcount += 1
            if col == "Orange":
                ocount += 1
            if col == "Blue White" or col == "Blue-white" or col == "Blue white " or col == "Blue white":
                bwcount += 1
            if col == "White" or col == "white":
                wcount += 1
            if col == "Whitish":
                wicount += 1
            if col == "Blue" or col == "Blue ":
                bcount += 1
            if col == "Yellowish White" or col == "yellow-white" or col == "White-Yellow":
                ywcount += 1
            if col == "'Pale yellow orange'":
                pyocount += 1
            if col == "Yellowish" or col == "yellowish":
                ycount += 1
            if col == "Orange-Red":
                orcount += 1
            for item in cat:
                if int(star[4]) == item:
                    if col == "Red":
                        raccuracy[item] += 1
                    if col == "Orange":
                        oaccuracy[item] += 1
                    if col == "'Blue White'" or col == "Blue-white" or col == "'Blue white '" or col == "'Blue white'":
                        bwaccuracy[item] += 1
                    if col == "White" or col == "white":
                        waccuracy[item] += 1
                    if col == "Whitish":
                        wiaccuracy[item] += 1
                    if col == "Blue" or col == "'Blue '":
                        baccuracy[item] += 1
                    if col == "Pale yellow orange":
                        pyoaccuracy[item] += 1
                    if col == "'Yellowish White'" or col == "yellow-white" or col == "White-Yellow":
                        ywaccuracy[item] += 1
                    if col == "Yellowish" or col == "yellowish":
                        yaccuracy[item] += 1
                    if col == "Orange-Red":
                        oraccuracy[item] += 1
                                
                    
# FIND BEST COMBO FOR EACH COLOR, TYPE --> ADD UP TOTAL ERROR
print("\nFIND THE BEST COMBO FOR EACH (COLOR, TYPE)...")
raccuracy[:] = [x / rcount for x in raccuracy]
oaccuracy[:] = [x / ocount for x in oaccuracy]
bwaccuracy[:] = [x / bwcount for x in bwaccuracy]
waccuracy[:] = [x / wcount for x in waccuracy]
wiaccuracy[:] = [x / wicount for x in wiaccuracy]
baccuracy[:] = [x / bcount for x in baccuracy]
ywaccuracy[:] = [x / ywcount for x in ywaccuracy]
yaccuracy[:] = [x / ycount for x in yaccuracy]
pyoaccuracy[:] = [x / pyocount for x in pyoaccuracy]
oraccuracy[:] = [x / orcount for x in oraccuracy]

final_list = [raccuracy, oaccuracy, bwaccuracy, waccuracy, wiaccuracy, baccuracy, ywaccuracy, yaccuracy, pyoaccuracy, oraccuracy]
print("\nList of Accuracies for Combinations:   " + str(final_list))

total_error = 0
dict_attribute = dict()
for item in final_list:
    index = item.index(max(item))
    total_error += (1-item[index])
    
dict_attribute = {
    "Red": 0,
    "Orange": 5,
    "BW": 3,
    "White": 2,
    "Whitish": 3,
    "Blue": 4,
    "Yellowish-white": 3,
    "Yellow": 3,
    "Pale Yellow Orange": 0,
    "Orange-Red": 3
    }

print("\nTotal Error of Best Rules (Attribute = Color):  " + str(total_error))


# TESTING DATASET
print("\n\nTESTING DATASET")
file = open('star_data_test.csv')
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

# MAKE DATASET
count = 0
acc = 0
for star in rows:
    count += 1
    star_info = (math.log10(float(star[0])), math.log10(float(star[1])), math.log10(float(star[2])), float(star[3]), star[4], star[5], star[6])
    if star_info[5] == "Red" and star_info[4] == 0:
        acc += 1
    elif star_info[5] == "Orange" and star_info[4] == 5:
        acc += 1
    elif star_info[5] == "'Blue White'" or star_info[5] == "Blue-white" or star_info[5] ==  "'Blue white '" or star_info[5] == "'Blue white'" and star_info[4] == 3:
        acc += 1
    elif star_info[5] == "White" or star_info[5] ==  "white" and star_info[4] == 2:
        acc += 1
    elif star_info[5] == "Whitish" and star_info[4] == 3:
        acc += 1
    elif star_info[5] == "Blue" and star_info[4] == 4:
        acc += 1
    elif star_info[5] == "Pale yellow orange" and star_info[4] == 3:
        acc += 1
    elif star_info[5] == "'Yellowish White'" or star_info[5] == "yellow-white" or star_info[5] ==  "White-Yellow" and star_info[4] == 3:
        acc += 1
    elif star_info[5] == "Yellowish" or star_info[5] ==  "yellowish" and star_info[4] == 0:
        acc += 1
    elif star_info[5] == "Orange-Red" and star_info[4] == 3:
        acc += 1


print("Accuracy Achieved:  " + str(float((count-acc)/count)))

