# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Counting Instructions

# File: countfib.py
# This program will print the number of a recursive Fibonacci
# function with problem sizes that double

from counter import Counter

def fib (n, counter):
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib (n-1, counter) + fib(n-2, counter)

problemSize = 2
print("%12s%15s" % ("ProblemSize", "Calls"))
for count in range(5):
    counter = Counter
    # This marks the START of the algorithm
    fib(problemSize, counter)
    # This mark the END of the algorithm
    print("%12d%15s" % (problemSize, counter))
    problemSize *= 2

