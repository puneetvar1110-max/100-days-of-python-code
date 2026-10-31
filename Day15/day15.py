# Day 17: 100 Days of Python
# Topic: Armstrong Number
# Description: Check whether a number is an Armstrong number or not.

number = int(input("Enter the number: "))
strnum = str(number)
numlen = len(strnum)
result = 0

for i in strnum:
    result = int(i) ** numlen + result

if result == number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")