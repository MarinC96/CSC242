# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Basic Sort Algorithms - (NO OUTPUT - BLANK CODE)

# File: basicsort.py

# This program demonstrates a basic sorting algorithm as
# most python sort functions will rely on the use of swap

def swap(lyst, i, j):
    # Exchanges the items at positions i and j.
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j]

# This will go above the definitions of a particular sort algorithm.