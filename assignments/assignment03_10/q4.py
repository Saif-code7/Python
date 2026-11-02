"""Q4. Product of Digits

Take an integer N as input and 
calculate the product of all its digits.

Example:
Input: 234
Output: 24
"""
n = int(input("enter your number:- "))
p = 1
if n ==0:
    print(0)

else:
    while n>0:
            ld = n%10
            p = p*ld
            n = n//10
    
print(p)
