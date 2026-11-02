"""
# Q3. Check Strong Number 
#
# Take an integer N as input and
# check whether it is a Strong Number.
# A Strong Number is a number
# whose sum of factorials of its
# digits equals the original number.
#
# Example:
# Input: 145
# 1! = 1
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# Sum: 1 + 24 + 120 = 145
# Output: Strong Number
"""

N= int(input("enter a number:- "))

sum =0
n = N
ld = 0

while N>0:
        ld = N%10
        fact = 1
        for i in range(1,ld+1):
              fact = fact*i
        sum = sum +fact
        N = N//10

print(sum)
if sum == n:
       print("strong number")
else:
       print("not a strong number")
        
         




