# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Sequential Search of a List - (NO OUTPUT - BLANK CODE)

# File: seqsearch.py
# This program will search through a list of items (going through all items) until it
# finds the target value.


def sequentialSearch(target,lyst):
    # Returns the position of the target item if found, or -1 otherwise.
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return - 1
