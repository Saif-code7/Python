"""
# Q1. Count Numbers Divisible by Both 3 and 5
#
# Take an integer N as input and count how many numbers from 1 to N
# are divisible by both 3 and 5 (multiples of 15).
#
# Example:
# Input: 35
# Output: 2
# (Explanation: The numbers are 15 and 30. Total count = 2)
"""



N=int(input("enter your number:- "))
count = 0
for i in range(1,N+1):
    if i%3 == 0 and i%5 == 0:
        count += 1
print(count)


