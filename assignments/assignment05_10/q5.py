"""Q5. Check Number
Create a function check_number() that takes a number 
and checks whether it is Positive, Negative, or Zero.

Example:
Input: -8
Output: Negative
"""

def check_number(n):
    if n>0:
        return "positive"
    elif n == 0:
        return "number is zero"
    else :
        return "negative"

a = int(input("enter your number:- "))
print(check_number(a))