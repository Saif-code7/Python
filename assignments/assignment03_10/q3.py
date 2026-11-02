"""Q3. Count Digits Greater Than 5

Take an integer N as input and count how many digits in the number are greater than 5.

Example:
Input: 583721
Output: 2
"""
n = int(input("enter your number:- "))
count =0
while n>0:
    ld = n%10
    if ld >5:
        count += 1
    n = n//10
print(count)