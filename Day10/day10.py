
# Day 11: 100 Days of Python
# Topic: Check Whether a Number Is Prime
# Description: Determine whether a number is prime.

number = int(input("Enter the number: "))
isprime = True

if number < 2:
    isprime = False
else:
    for i in range(2, number):
        if number % i == 0:
            isprime = False
            break

if isprime:
    print(number, "is a Prime number")
else:
    print(number, "is not a Prime number")
