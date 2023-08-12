#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:11:05 2022

@author: lynntao
"""
from  math  import  log 
import random
import sys

original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(text, cipher):
    text = text.upper()
    for i in range(0,len(text)):
        if text[i].isalpha():
           index = original.index(text[i])
           text = text[:i] + cipher[index] + text[i+1:]
    return text


def decode(code_text, cipher):
    code_text = code_text.upper()
    for i in range(0,len(code_text)):
        if code_text[i].isalpha():
           index = cipher.index(code_text[i])
           code_text = code_text[:i] + original[index] + code_text[i+1:]
    return code_text


def fitness_function(n, code_text, candidate_cipher, n_gram_eng):
    text = decode(code_text, candidate_cipher)
    n_grams_freq = []
    
    for i in range(0,len(code_text)-n):
        if text[i:i+n].isalpha():
            if text[i:i+n] in n_gram_eng.keys():
                n_grams_freq.append(log(int(n_gram_eng[text[i:i+n]]), 2))
  
    return sum(n_grams_freq)
        
    
def hill_climbing(code_text):
    candidate = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = fitness_function(4, code_text, candidate, n_gram_eng)
    while 1 > 0:
        new_cipher = swap_letters(candidate)
        new_score = fitness_function(4, code_text, new_cipher, n_gram_eng)
        text = decode(code_text, new_cipher)
        # print(new_score)
        # print(text)
        # print("\n\n")
        if new_score > score:
            score = new_score
            candidate = new_cipher
            text = decode(code_text, new_cipher)
            print(new_score)
            print(text)
            print("\n\n")
            
            
def swap_letters(candidate):
    swap = random.randint(0, 25)
    a = candidate[swap]
    reverse = random.randint(0, 25)
    while reverse == swap:
        reverse = random.randint(0, 25)
    b = candidate[reverse]
    new_cipher = candidate[0:swap] + b + candidate[swap+1:]
    new_cipher = new_cipher[0:reverse] + a + new_cipher[reverse+1:]
    return new_cipher


n_gram_eng = dict()
with open("ngrams.txt", encoding='utf-8-sig') as f:
    f = f.read().split("\n")
    for i in range(0,len(f)-1):
        index = f[i].index(" ")
        n_gram = f[i][:index]
        count = f[i][index+1:]
        n_gram_eng[n_gram] = count


# GENETIC ALGORITHM
def all_letters(child):
    original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for item in original:
        if item not in child:
            return False
    return True


def population():
    pop = []
    original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while len(pop)<500:
        new = ''.join(random.sample(original,len(original)))
        if new not in pop:
            pop.append(new)
    return pop


def Sort(pos_heuristic):
    pos_heuristic.sort(key = lambda x: x[1], reverse = True)
    return pos_heuristic


def selection(population, coded_text, NUM_CLONES, TOURNAMENT_SIZE, TOURNAMENT_WIN_PROBABILITY, CROSSOVER_LOCATIONS, MUTATION_RATE):
    next_gen = []
    rank_current = []
    rank_dict = dict()
    for item in population:
        score = fitness_function(4, coded_text, item, n_gram_eng)
        rank_current.append([item, score])
        rank_dict[item] = score
    rank_current = Sort(rank_current)
    for i in range(0, NUM_CLONES):
        next_gen.append(rank_current[i][0])
    
    print(decode(coded_text, rank_current[i][0]))
      
    
    while len(next_gen) < 500:
        parents = random.sample(population, 2*TOURNAMENT_SIZE)
        tourn1 = parents[:TOURNAMENT_SIZE]
        tourn2 = parents[TOURNAMENT_SIZE:]
        parent1 = tournament(tourn1, rank_dict, TOURNAMENT_WIN_PROBABILITY)
        parent2 = tournament(tourn2, rank_dict, TOURNAMENT_WIN_PROBABILITY)
        
        child = breed(parent1, parent2, CROSSOVER_LOCATIONS)
        child = mutation(child, MUTATION_RATE)
    
        if child not in next_gen:
            next_gen.append(child)
        
    return next_gen
    
    
def tournament(tourn, rank_dict, TOURNAMENT_WIN_PROBABILITY):
    rank_tourn = []
    for item in tourn:
        rank_tourn.append([item, rank_dict[item]])
    rank_tourn = Sort(rank_tourn)
    
    for cipher in rank_tourn:
        if random.random() < TOURNAMENT_WIN_PROBABILITY:
            return cipher[0]
    

def breed(parent1, parent2, CROSSOVER_LOCATIONS):
    child = []
    for i in range(0, 26): 
        child.append(0)
    locations = random.sample(range(0, 26),  CROSSOVER_LOCATIONS)
    for pos in locations:
        child[pos] = parent1[pos]
    
    for j in range(0, 26):
        if parent2[j] not in child:
            index = child.index(0)
            child[index] = parent2[j]
        
    if all_letters(child):
        return "".join(child)


def mutation(child, MUTATION_RATE):
    if random.random() < MUTATION_RATE:
        child = swap_letters(child)
    return child
    


# PARAMETERS
POPULATION_SIZE  =  500
NUM_CLONES = 1
TOURNAMENT_SIZE  =  20
TOURNAMENT_WIN_PROBABILITY  =  .75
CROSSOVER_LOCATIONS  =  5
MUTATION_RATE  =  .8

text = "".join(sys.argv[1:])


# text = """"
# ZFNNANWJWYBZLKEHBZTNSKDDGJWYLWSBFNSSJWYFNKBGLKOCNKSJEBDWZFNGKLJKJNQFJPFJBXHBZTNRDKNZFNPDEJWYDRPDEGCNZNWJ YFZZFLZTCNBBNBZFNNLKZFSLKONWBLCCKJANKBPHGBZFNGNLOBLWSRDCSBZFNRJWLCBFDKNJWLWSWDTDSUWDTDSUOWDQBQFLZBYDJWYZ DFLGGNWZDLWUTDSUTNBJSNBZFNRDKCDKWKLYBDRYKDQJWYDCSJZFJWODRSNLWEDKJLKZUJNANWZFJWODRDCSSNLWEDKJLKZUZFNRLZFN KQNWNANKRDHWSJZFJWODRSNLWEDKJLKZU
# """

population = population()
for i in range(0, 500):
    print(i)
    population = selection(population, text, NUM_CLONES, TOURNAMENT_SIZE, TOURNAMENT_WIN_PROBABILITY, CROSSOVER_LOCATIONS, MUTATION_RATE)



    
    
    
    
    

