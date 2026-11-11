# Day 25: 100 Days of Python
# Topic: Spy Number
# Description: Check whether a number is a Spy Number or not.
#
# What is a Spy Number?
# A number whose sum of digits is equal to the product of its digits.
#
# Example:
# 1124
# Sum = 1 + 1 + 2 + 4 = 8
# Product = 1 * 1 * 2 * 4 = 8
# Therefore, 1124 is a Spy Number.

number = int(input("Enter the number: "))
temp = number
add = 0
multiply = 1

while temp != 0:
    last = temp % 10
    add += last
    multiply *= last
    temp = temp // 10

if number > 0 and add == multiply:
    print(f"{number} is a Spy Number")
else:
    print(f"{number} is not a Spy Number")