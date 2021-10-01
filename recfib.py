# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Exponential Algorithm: Recursive Fibonacci - (NO OUTPUT - BLANK CODE)
# File: recfib.py

def fib(n):
    # The recursive Fibonacci function
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
