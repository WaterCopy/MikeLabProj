# Bitwise n-gram preprocessing version 0.1 (8/6/19)  Tim Brailsford

from builtins import map
from builtins import range
import binascii
import itertools

# returns binary representation of a string (without the 2-character header)
def text2bin(str):
    binStr = bin(int(binascii.hexlify(str.encode('ascii')), 16))
    return binStr[2:]

# converts string of 8-bit binary characters to 7-bt binary characters (e.g. for ASCII)
def convert7bit(str):
    output=""
    for i in range(0, len(str)):
        output=output+str[:7]
        str=str[8:]
    return output

# returns n-grams
def nGram(n):
    grams=2**n # number of permutations
    output=[]

    # create search patterns for n (i.e. 1-gram, 2-gram, 3-gram etc.)
    patterns = []
    for x in map(''.join, itertools.product('01', repeat=n)):
        patterns.append(x)

    return patterns

# count overlapping substrings in string
def overlapCount(str, substr):
    n = 0
    i = 0
    while True:
        i = str.find(substr, i)
        if i >=0:
            n +=1
            i +=1
        else:
            break
    return n


# returns n-gram frequencies for str (overlapping n-grams)
def nGramFrequencies(str, n):
    grams=2**n # number of permutations
    output=[]

    # create search patterns for n (i.e. 1-gram, 2-gram, 3-gram etc.)
    patterns = []
    for x in map(''.join, itertools.product('01', repeat=n)):
        patterns.append(x)
            
    # loop through permutations
    for i in range(0,grams):        
        pCount = overlapCount(str, patterns[i])
        output.append(pCount)
        
    return output


# returns n-gram frequencies for str (overlapping n-grams)
def nGramRelFrequencies(binaryStr, n, strLength):
    grams=2**n # number of permutations
    output=[]

    # create search patterns for n (i.e. 1-gram, 2-gram, 3-gram etc.)
    patterns = []
    for x in map(''.join, itertools.product('01', repeat=n)):
        patterns.append(x)
            
    # loop through permutations
    for i in range(0,grams):        
        # count occurrences of n-gram
        pCount = overlapCount(binaryStr, patterns[i])
        
        # cast to float and adjust for file length
        pCount=float(pCount)
        pCount=pCount/strLength
        
        output.append(pCount)
        
    return output


