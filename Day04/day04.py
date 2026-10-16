# Day 4: 100 Days of Python
# Topic: Maximum number finder
# Description: Checks the maximum number among 3 number.

a = int(input("Enter First Number \n"))
b = int(input("Enter Second Number \n"))
c = int(input("Enter Third Number \n"))
if(a>=b and a>=c):
    print(a,"is greater \n")
elif(b>=c):
    print(b,"is greater \n")
else:
    print(c,"is greater \n")
