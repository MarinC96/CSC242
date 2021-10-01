# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Measuring the Run Time of an Algorithm

# File: timing1.py
# This program will print the running times for a problem size that double
# using a single loop.

import time

problemSize = 10000000
print("%12s%16s" % ("ProblemSize", "Seconds"))
for count in range (5):
    start = time.time()
    # This marks the START of the algorithm
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    # This marks the END of the algorithm
    elapsed = time.time() - start
    print("%12s%16.3f" % (problemSize, elapsed))
    problemSize *= 2
    