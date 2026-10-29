# Day 14: 100 Days of Python
# Topic: Count Digits
# Description: Count the digits in an integer.

number = int(input("Enter the number: "))
count = 0

if number < 0:
    number = -number

for digit in str(number):
    count += 1

print("Number of digits:", count)