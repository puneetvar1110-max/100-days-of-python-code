# Day 22: 100 Days of Python
# Topic: Strong Numbers in a Range
# Description: Find all Strong Numbers within a given range.
#
# What is a Strong Number?
# A Strong Number is equal to the sum of factorials of its digits.
#
# Example:
# 145 = 1! + 4! + 5!
#     = 1 + 24 + 120
#     = 145

range1 = int(input("Enter the starting range: "))
range2 = int(input("Enter the ending range: "))

for i in range(range1, range2 + 1):
    ori = i
    result = 0

    while i != 0:
        last = i % 10
        fact = 1

        for j in range(1, last + 1):
            fact = fact * j

        result = result + fact
        i = i // 10

    if ori > 0 and ori == result:
        print(f"{ori} is a Strong Number")