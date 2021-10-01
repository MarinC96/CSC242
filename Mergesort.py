# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Mergesort - (NO OUTPUT - BLANK CODE)
# File: mergesort.py

from Arrays.arrays import Arrays

def mergesort(lyst):
    # lyst is being sorted
    # copyBuffer temporary space needed during merge
    copyBuffer = Arrays(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst) - 1)

def mergeSortHelper(lyst, copyBuffer, low, high):
    # lyst list is being sorted
    # copyBuffer temp space needed during merge
    # low, high bounds of sublist
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)

def merge(lyst, copyBuffer, low, middle, high):
    # lyst list that is being sorted
    # copyBuffer temp space needed during the merge process
    # low beginning of first sorted sublist
    # middle end of first sorted sublist
    # middle +1 beginning of second sorted sublist
    # high end of second sorted sublist
    # Initialize i1 and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1
    # Interleave items from the sublist into the
    # copyBuffer in such a way that order is maintained
    for i in range (low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2] # First sublist exhausted
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1] # Second sublist exhausted
            i1 += 1
        elif copyBuffer[i] < lyst[i2]: # Item in first sublist <
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2] # Item in second sublist <
            i2 += 1
    for i in range(low, high + 1): # Copy sorted items back to
        lyst[i] = copyBuffer[i] # proper position in list