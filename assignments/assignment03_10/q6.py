"""Q6. Count Digits Divisible by 3

Take an integer N as input and count how many
digits are divisible by 3, including 0.

Example:
Input: 93621
Output: 3
"""
n = int(input("enter your number:- "))
count = 0
while n>0:
    l = n%10
    if l%3 == 0:
        count += 1
    n = n//10
print(count)