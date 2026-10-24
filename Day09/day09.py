# Day 9: 100 Days of Python
# Topic: Factorial of Any Number
# Description: Calculate the factorial of a number.

number = int(input("Enter the number: "))

factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, number + 1):
        factorial *= i

    print(f"The factorial of {number} is {factorial}")
