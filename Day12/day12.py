# Day 12: 100 Days of Python
# Topic: Reverse a Number
# Description: Reverse an integer using a while loop.

number = int(input("Enter the number: "))
rev = 0

while number != 0:
    last = number % 10       # Get the last digit
    rev = rev * 10 + last    # Add digit to reversed number
    number = number // 10    # Remove the last digit

print("Reversed number:", rev)
