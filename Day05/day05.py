
# Day 5: 100 Days of Python
# Topic: Age Eligibility Checker
# Description: Check whether a person can vote.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(name, "You are eligible to vote.")
else:
    print(name, "You are not eligible to vote.")
