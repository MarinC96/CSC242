# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Search for the Minimum - (NO OUTPUT - BLANK CODE)

# File: minsearch.py
# This program will search for the smallest item within a list

def indexOfMin(lyst):
    # Returns the index of the minimum item
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

