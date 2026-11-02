"""Q4. Reverse a Number
Create a function reverse_number() that 
takes a number and returns its reverse.

Example:
Input: 1234
Output: 4321
"""

def reverse_number(n):
    ld = 0
    s = 0
    while n>0:
        ld = n%10
        s = s*10+ld
        n = n//10
    return s

a = int(input("enter your number:- "))
print(reverse_number(a))