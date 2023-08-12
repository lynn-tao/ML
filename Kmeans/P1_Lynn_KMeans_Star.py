#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:13:01 2022

@author: lynntao
"""

import csv
import math
import random

# READ FILE
file = open('K-Means/star_data.csv')
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

# MAKE DATASET
star_type = dict()
dataset = []
for star in rows:
    star_info = (math.log10(float(star[0])), math.log10(float(star[1])), math.log10(float(star[2])), float(star[3]))
    dataset.append(star_info)
    star_type[star_info] = star[4]
# print(dataset)
# print(star_type)

# K MEANS ALGORITHMS
def distance(star1, star2):
    dist = math.sqrt((star1[0] - star2[0])**2 +(star1[1] - star2[1])**2 +(star1[2] - star2[2])**2 +(star1[3] - star2[3])**2)
    return dist

def closest_mean(parents, star):
    distances = []
    for item in parents:
        distances.append(distance(item, star))
    min_dist = min(distances)
    index = distances.index(min_dist)
    closest_parent = parents[index]
    return closest_parent
    
# log(Temperature), log(Luminosity), log(Radius), Absolute Visual Magnitude
def find_average(star_list):
    temp = 0
    lumin = 0
    rad = 0
    avm = 0
    for item in star_list:
        temp += item[0]
        lumin += item[1]
        rad += item[2]
        avm += item[3]
    average = (temp/len(star_list), lumin/len(star_list), rad/len(star_list), avm/len(star_list))
    return average

# K MEANS ALGO
K = 6
parents = random.sample(dataset, K)


og_means = dict()
for item in parents:
    og_means[item] = []
for star in dataset:
    closest_parent = closest_mean(parents, star)
    og_means[closest_parent].append(star)

new_parents = []
for item in og_means.keys():
    new_parents.append(find_average(og_means[item]))


while new_parents is not parents:
    parents = new_parents
    og_means = dict()
    for item in parents:
        og_means[item] = []
    for star in dataset:
        closest_parent = closest_mean(parents, star)
        og_means[closest_parent].append(star)

    for item in og_means.keys():
        new_parents.append(find_average(og_means[item]))
        


for item in og_means.keys():
    print(item)
    stars = []
    for star in og_means[item]:
        stars.append(star_type[star])
    print(stars)

    
    

















