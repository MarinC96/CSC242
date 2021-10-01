# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Insertion Sort - (NO OUTPUT - BLANK CODE)
# File: insertionsort.py

def swap(lyst, i, j):
    # Exchanges the items at positions i and j.
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j]

def insertionSort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
            else:
                break
            lyst[j + 1] = itemToInsert
            i += 1
