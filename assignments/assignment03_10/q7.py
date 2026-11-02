"""Q7. Replace Every Digit with 9

Take an integer N as input and create a new number by replacing every digit with 9.

Example:
Input: 1234
Output: 9999
"""
n = int(input("enter your number:- "))
s = 0
while n>0:
    l = n%10 
    l = 9
    s = s*10+l
    n = n//10
print(s)


# optimised

n = int(input("enter: -"))
s = 0
while n >0:
    ld = n%10
    if ld != 9:
        ld = 9
    s = s*10+ld
    n = n//10
print(s)