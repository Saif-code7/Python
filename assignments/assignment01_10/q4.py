'''Q4. Check Perfect Number

Take an integer N as input and check whether it is a perfect number.

A perfect number is a number whose proper factors add up to the number itself.

Example:
Input: 6
Output: Perfect Number
'''

N = int(input("tell your number:- "))
sum = 0
for i in range(1,N):
    if N%i == 0:
        sum += i
if sum == N:
    print(f"{N} is a perfect number ")
else:
    print(f"{N} is not a perfect number")
