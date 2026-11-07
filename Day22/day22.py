# Day 22: 100 Days of Python
# Topic: Automorphic Numbers in a Range
# Description: Find all Automorphic Numbers within a given range.
#
# What are Automorphic Numbers?
# Numbers whose squares end with the same digits as the original numbers.
#
# Example:
# 25 * 25 = 625
# The square ends with 25.
# Therefore, 25 is an Automorphic Number.

range1 = int(input("Enter the starting range: "))
range2 = int(input("Enter the ending range: "))

for i in range(range1, range2 + 1):
    square = i * i
    numlen = len(str(i))
    last = square % (10 ** numlen)

    if last == i and i >= 0:
        print(f"{i} is an Automorphic Number")