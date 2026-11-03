# Day 18: 100 Days of Python
# Topic: Perfect Numbers in a Range
# Description: Find all Perfect Numbers within a given range.
#
# What is a Perfect Number?
# A Perfect Number is equal to the sum of all its proper divisors.
#
# Example:
# 6 = 1 + 2 + 3

range1 = int(input("Enter the range 1: "))
range2 = int(input("Enter the range 2: "))

for i in range(range1, range2 + 1):
    result = 0

    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            result += j

    if i > 0 and i == result:
        print(i, "is a Perfect Number")