#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:49:19 2022

@author: stevenhartinger
"""

import hashlib
import random
from re import I
import string
import time

def splitHash(hash):
    if len(hash)> 50:
        hash = hash[0:9]
    return hash
            
def compareHash():
    isFound = False
    count = 0
    starttime = time.time()

    dictionary = {}
    N = random.randint(1,100)
    arbitrary_string1 = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))

    hash_string1 = hashlib.sha256(arbitrary_string1.encode())
    hash_string1 = hash_string1.hexdigest()
    hash_string1 = splitHash(hash_string1)         
    dictionary = {arbitrary_string1 : hash_string1}
    tempDic = {}
    while isFound != True:
        count += 1
        dictionary.update(tempDic)
        N = random.randint(1,100)
        arbitrary_string1 = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
        for word, hash in dictionary.items():
                if word != arbitrary_string1:
                     hash_string1 = hashlib.sha256(arbitrary_string1.encode())
                     hash_string1 = hash_string1.hexdigest()
                     hash_string1 = splitHash(hash_string1)   
                
                     if hash == hash_string1:
                        isFound = True
                        print(hash)
                        print(hash_string1)
                        endtime = time.time()
                        print(endtime - starttime)
                        print("Inputs: ", count)
                     else:
                        tempDic = {arbitrary_string1 : hash_string1}
                else:
                    break      
compareHash()
        










