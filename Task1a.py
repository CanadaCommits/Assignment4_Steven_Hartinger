
import hashlib
import random
from re import I
import string
import time
#a
arbitrary_string = input("Enter a String: ")

hash_string =hashlib.sha256(arbitrary_string.encode())

print(hash_string.hexdigest())

#b
string1 = "ichtestedasaus"

string2 = "ichtestedasauch"

def hammingDist(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count

print(hammingDist(string1, string2))


hash_string1 = hashlib.sha256(string1.encode())
hash_string2 = hashlib.sha256(string2.encode())


hash_string1 = hash_string1.hexdigest()
hash_string2 = hash_string2.hexdigest()

print("hash1: ", hash_string1)
print("hash2: ", hash_string2)
