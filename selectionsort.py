# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Selection Sort- (NO OUTPUT - BLANK CODE)
# File: selectionsort.py

def swap(lyst, i, j):
    # Exchanges the items at positions i and j.
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j]

def selectionSort(lyst):
    i = 0
    while i <len(lyst) - 1: # This does n-1 searches
        minIndex = i # For the smallest
        j = i + 1
        while j < len(lyst): # Starts a search
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex !=i: # Exchange if needed
            swap(lyst, minIndex, i)
        i += 1
        