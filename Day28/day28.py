# Day 28: 100 Days of Python
# Topic: Count Even and Odd Numbers in a List
# Description: Count even and odd numbers using a loop.


numbers = []
even = 0
odd = 0

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers:", even)
print("Odd Numbers:", odd)