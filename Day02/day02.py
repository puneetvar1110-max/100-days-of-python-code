
# Day 2: 100 Days of Python
# Topic: Even or Odd Number Checker
# Description: Checks whether a number is even or odd using the modulo operator (%).


number = int(input("Enter a number: "))

if number % 2 == 0: # The modulo operator (%) gives the remainder when one number is divided by another.
    print(number, "is an Even Number")
else:
    print(number, "is an Odd Number")
