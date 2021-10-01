# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Binary Search of a Sorted List - (NO OUTPUT - BLANK CODE)

# This program will split a list into two and search both halves of such list
# until the target value is found. The list is split at the mid point.

def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
        return - 1

    