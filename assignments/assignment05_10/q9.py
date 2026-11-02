"""Q9. Find Factorial
Create a function factorial() that takes a 
number and returns its factorial.

Example:
Input: 5
Output: 120
"""

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

num = int(input("enter your number:- "))
print(factorial(num))
