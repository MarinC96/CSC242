# CSC 242
# Chapter 3: Searching, Sorting, and Complexity

# Comparing Data Items - (SAVINGS ACCOUNT - EXAMPLE)

# File: comparingdata.py
# This program is an example of how one can use classes, definitions and operators
# to establish and determine relationships between data items.

class SavingsAccount(object):
    # This class represents a savings account with the owner's name, PIN, and balance.

    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __lt__(self, other):
        return self.name < other.name

    # Other methods, including __eq__


s1 = SavingsAccount("Ken", "1000", 0)
s2 = SavingsAccount("Bill, 1001", 30)

print("s1 < s2")
print(s1 < s2, "\n")

print("S2 < s1")
print(s2 < s1, "\n")

print("s1 > s2")
print(s1 > s2, "\n")

print("s2 > s1")
print(s2 > s1, "\n")

print("s2 == s1")
print(s2 == s1, "\n")

# The part below is supposed to be true, for some reason, this Python IDE will not recognize it as such
# unless I specifically declare that the variables are the same.

s3 = s1
print("s1 == s3")
print(s1 == s3, "\n")

s4 = s1
print("s4 == s1")
print(s4 == s1)
