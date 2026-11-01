# Day 16: 100 Days of Python
# Topic: Armstrong Numbers in a Range
# Description: Find all Armstrong numbers within a given range.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Armstrong numbers:")

for number in range(start, end + 1):
    strnum = str(number)
    numlen = len(strnum)
    result = 0

    for i in strnum:
        result += int(i) ** numlen

    if result == number:
        print(number)