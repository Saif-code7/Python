"""Q6. Check Equal First and Last Digit

Take an integer N as input and check whether its first digit and last digit are the same.

Example:

Input: 12341

Output: Same
"""
# N = int(input("enter your number"))   #12341
# while(N!=0):
#     last_digit = N%10 
#     N = N/10



# n = 12341
# a = str(n)#"12341"
# if a[0] == a[-1]:
#     print("Equal")
 

n  = 12341
n = str(n)

if n[0] == n[-1]:
    print("equal")