"""Q2. Check Even or Odd
Create a function check_even_odd() that takes 
a number and returns whether it is Even or Odd.

Example:
Input: 7
Output: Odd
"""


def check_even_odd(n):
    if n%2 == 0:
        return "even"
    else:
        return "odd"

a = int(input("enter your number:- "))
print(check_even_odd(a))