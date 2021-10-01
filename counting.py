# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Counting Instructions

# File: counting.py
# This program will print the number of iterations for problem
# sizes that double, using a nested loop

problemSize = 1000
print("%12s%15s" % ("ProblemSize", "Iterations"))
for count in range(5):
    number = 0
    # This marks the START of the algorithm
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1
    # This marks the END of the algorithm
    print("%12d%15d" % (problemSize, number))
    problemSize *= 2