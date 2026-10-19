# Day 7: 100 Days of Python
# Topic: Multiplication Table
# Description: Print the multiplication table for any number.

number = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")