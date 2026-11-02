"""Q6. Find GCD of Two Numbers
Create a function gcd() that takes two numbers and returns their Greatest Common Divisor (GCD).

Example:
Input: 24 36
Output: 12
"""

def gcd(n1,n2):
    large = 0
    for i in range(1,n1+1):
        if n1%i == 0 and n2%i ==0:
            large = i
    return large

num = int(input("enter your first number:- "))
num2 = int(input("enter your second number"))
print(gcd(num, num2))
