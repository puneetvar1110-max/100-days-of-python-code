# Day 25: 100 Days of Python
# Topic: Neon Number
# Description: Check whether a number is a Neon Number or not.
#
# What is a Neon Number?
# A Neon Number is a number whose square's digit sum
# is equal to the original number.
#
# Example:
# 9 * 9 = 81
# 8 + 1 = 9
# Therefore, 9 is a Neon Number.

number = int(input("Enter the number: "))
square = number * number
result = 0

while square != 0:
    last = square % 10
    result += last
    square = square // 10

if result == number and number >= 0:
    print(f"{number} is a Neon Number")
else:
    print(f"{number} is not a Neon Number")