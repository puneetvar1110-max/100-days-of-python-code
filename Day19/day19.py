# Day 19: 100 Days of Python
# Topic: Strong Number
# Description: Check whether a number is a Strong Number or not.
#
# What is a Strong Number?
# A Strong Number is equal to the sum of factorials of its digits.
#
# Example:
# 145 = 1! + 4! + 5!
#     = 1 + 24 + 120
#     = 145

number = int(input("Enter the number: "))
num = number
result = 0

while number != 0:
    last = number % 10
    fact = 1

    for i in range(1, last + 1):
        fact = i * fact

    result = result + fact
    number = number // 10

if num > 0 and num == result:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is not a Strong Number")