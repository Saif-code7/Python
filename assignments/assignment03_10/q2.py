"""Q2. Check Palindrome Number

Take an integer N as input and check whether the
 number remains the same when its digits are reversed.

Example:
Input: 121
Output: Palindrome
"""
N = int(input("enter your number:- "))
ld = 0
s = 0
a = N
while N>0:
    ld = N%10
    s = s*10+ld
    N = N//10
if s == a:
    print("palindrome number")
else:
    print("not a palindrome number")




    