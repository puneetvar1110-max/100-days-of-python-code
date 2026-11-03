# Day 17: 100 Days of Python
# Topic: Perfect Number
# Description: Check whether a number is a Perfect Number or not.
#
# What is a Perfect Number?
# A Perfect Number is a positive integer that is equal to
# the sum of all its proper divisors (excluding itself).
#
# Example:
# 6 = 1 + 2 + 3
# Therefore, 6 is a Perfect Number.

number = int(input("Enter the value: "))
result = 0

for i in range(1, (number // 2) + 1):
    if number % i == 0:
        result += i

if result == number and number > 0:
    print("Perfect Number")
else:
    print("Not a Perfect Number")