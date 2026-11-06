# Day 21: 100 Days of Python
# Topic: Automorphic Number
# Description: Check whether a number is an Automorphic Number or not.
#
# What is an Automorphic Number?
# A number whose square ends with the same digits as the original number.
#
# Example:
# 25 * 25 = 625
# The square ends with 25.
# Therefore, 25 is an Automorphic Number.

number = int(input("Enter the number: "))

square = number * number
numlen = len(str(number))

last = square % (10 ** numlen)

if last == number and number >= 0:
    print(f"{number} is an Automorphic Number")
else:
    print(f"{number} is not an Automorphic Number")