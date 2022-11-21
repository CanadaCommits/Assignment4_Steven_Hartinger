import string
import time
import random
import hashlib



# returns the digest of the hash
def hash_hex(input):
    hash = hashlib.sha256(input.encode('ascii'))
    digest = hash.hexdigest()
    return digest

def hamming_distance(str1, str2):
    i = 0
    count = 0

    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count

# returns the difference in digest bytes if hamming distance is 1
def get_difference(str1, str2):
    if (hamming_distance(str1, str2) == 1):
        hex1 = hash_hex(str1)
        hex2 = hash_hex(str2)
        length = len(hex1)
        diff = 0
        for i in range(length):
            if hex1[i] != hex2[i]:
                diff += 1
        return diff
    print("hamming distance is not 1")


# converts string to binary string
def str_to_bin(str):
    b_str = ""
    for char in str:
        b_str += format(char, "08b")
    return b_str


# finds if there are collisions between two different strings if your turncated the digest by n
def find_collisions(str1, str2, n):
    input = 1
    byte = n // 8
    bit = n % 8
    bits = get_turncated_bits(str1, str2, byte, bit)
    while (bits[0] != bits[1]):
        # str1 = random_str()
        str2 = random_str()
        bits = get_turncated_bits(str1, str2, byte, bit)
        input += 1
    return input


# get the turncated bits if (n is not base 16)
def get_turncated_bits(str1, str2, n, b):
    bit1 = ""
    bit2 = ""

    # getting the digest
    digest1 = hash_hex(str1)
    digest2 = hash_hex(str2)

    # truncate
    truncate1 = pad_byte(bin(int(digest1[:n], 16))[2:], (n * 8))
    truncate2 = pad_byte(bin(int(digest2[:n], 16))[2:], (n * 8))

    # getting the bits of the next byte
    byte1 = bin(int(digest1[(n + 1)], 16))[2:]
    byte2 = bin(int(digest2[(n + 1)], 16))[2:]

    byte1 = pad_byte(byte1[:b], 8)
    byte2 = pad_byte(byte2[:b], 8)

    bit1 += truncate1 + byte1
    bit2 += truncate2 + byte2

    return [bit1, bit2]


# pads the bits into a byte
def pad_byte(bits, l):
    bit = ""
    n = len(bits)
    if n != l:
        bit += "0" * (l - n)
        bit += bits
        return bit

    else:
        return bits


# creates a random string
def random_str():
    N = 11
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res


str1 = random_str()
str2 = random_str()
if str1 != str2:
    n = 50# num of bits
    st = time.time()
    inputs = find_collisions(str1, str2, n)
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds for ' + str(n) + " bits")
    print("num of inputs: " + str(inputs))