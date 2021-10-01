# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Bubble Sort - (NO OUTPUT - BLANK CODE)
# File: bubblesort.py

def swap(lyst, i, j):
    # Exchanges the items at positions i and j.
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j]

def bubbleSortWithTweak(lyst):
    n = len(lyst)
    while n>1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]: # Exchange needed if
                swap(lyst, i, i - 1)
                swapped = True
            i += 1
        if not swapped: return # Return if no swaps
        n -= 1
