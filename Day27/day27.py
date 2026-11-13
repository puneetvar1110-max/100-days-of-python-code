# Day 27: 100 Days of Python
# Topic: Find Largest and Smallest Number in a List
# Description: Find the largest and smallest elements using a loop.
#
# What is a List?
# A List is used to store multiple values in a single variable.

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest Number:", largest)
print("Smallest Number:", smallest)