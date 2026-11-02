"""Q1. Difference between Sum of Odd numbers and Sum of Even Numbers

Take an integer N as input. Calculate the sum of even numbers
and the sum of odd numbers from 1 to N, then find the difference between the two sums.

Example:
Input: 5
Output: 3
"""

N = int(input("enetr your number:- "))
sum_even = 0
sum_odd = 0
for i in range(1,N+1):
    if i%2 == 0:
        sum_even += i #2+4
    else:
        sum_odd += i # 1+3+5
print(sum_odd - sum_even)