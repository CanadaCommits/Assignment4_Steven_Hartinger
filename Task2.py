#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:25:43 2022

@author: stevenhartinger
"""

from bcrypt import *
from nltk.corpus import words
import nltk

# hashpw(<plaintext word>, <29-char salt for bcrypt>)
print(hashpw(b"registrationsucks", b"$2b$08$J9FW66ZdPI2nrIMcOxFYI."))

wordlist = words.words()

print(len(wordlist))


for word in wordlist:
    if len(word) <= 6 or len(word) >= 10:
        wordlist.remove(word)

print(len(wordlist))



        
