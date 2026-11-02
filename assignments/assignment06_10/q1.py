"""Q1. Find the Largest of Three Numbers
Create a function largest() that takes three numbers and returns the largest number.

Example:
Input: 12 45 23
Output: 45
"""

def largest(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3

a = int(input("enter first number:- "))
b = int(input("enter first number:- "))
c = int(input("enter first number:- "))

print(largest(a,b,c))