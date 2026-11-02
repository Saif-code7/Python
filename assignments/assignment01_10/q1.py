'''Q1. Count Numbers Divisible by 3

Take an integer N as input and count how many numbers from 1 to N are divisible by 3.

Example:
Input: 15
Output: 5
'''

N = int(input("enter your number:- "))
count = 0
for i in range(1,N+1):
    if i%3 == 0:
        count += 1
print(count)

