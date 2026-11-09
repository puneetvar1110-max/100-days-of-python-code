number = int(input("Enter the number"))
square = number*number
result = 0

while(number!=0):
    last = number%10
    result += last
    square = square//10
if result == number and number >= 0:
    print(f"{number} is a Neon Number")
else:
    print(f"{number} is not a Neon Number")
