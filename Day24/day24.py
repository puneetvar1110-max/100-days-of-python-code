# Day 24: 100 Days of Python
# Topic: Neon Numbers in a Range
# Description: Find all Neon Numbers within a given range.
#
# What are Neon Numbers?
# Numbers whose square's digit sum is equal to the original number.
#
# Example:
# 9 * 9 = 81
# 8 + 1 = 9
# Therefore, 9 is a Neon Number.

range1 = int(input("Enter the starting range: "))
range2 = int(input("Enter the ending range: "))

for i in range(range1, range2 + 1):
    square = i * i
    result = 0

    while square != 0:
        last = square % 10
        result += last
        square = square // 10

    if i >= 0 and result == i:
        print(f"{i} is a Neon Number")