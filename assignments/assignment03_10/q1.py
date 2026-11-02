"""Q1. Reverse a Number

Take an integer N as input and print its reverse.

Example:
Input: 12345
Output: 54321
"""

N = int(input("enter your number:- "))
last_d = 0
s = 0
while N>0:
    last_d = N%10
    s = s*10+last_d
    N = N//10
print(s)

"""N = int(input("enter your number:- "))
while N>0:
    print(N%10,end="")
    N = N//10"""