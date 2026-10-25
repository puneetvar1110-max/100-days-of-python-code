
# Day 11: 100 Days of Python
# Topic: Print Prime Numbers in a Range
# Description: Print all prime numbers between r1 and r2.

r1 = 2
r2 = 20

for i in range(r1, r2 + 1):
    isprime = True

    # Check whether i is divisible by any number from 2 to i-1
    if i < 2:
        isprime = False
    else:
        for j in range(2, i):
            if i % j == 0:
                isprime = False
                break

    # Print only prime numbers
    if isprime:
        print(i)
