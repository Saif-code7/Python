"""
# Q9. Check Harshad (Niven) Number
# Take an integer N as input and 
# check whether it is a Harshad Number.
# A Harshad number is a number 
# that is completely divisible by the sum of its digits.
#
# Example 1:
# Input: 18  -> Sum of digits: 1 + 8 = 9 -> 18 % 9 == 0
# Output: Harshad Number
# Example 2:
# Input: 14  -> Sum of digits: 1 + 4 = 5 -> 14 % 5 != 0
# Output: Not a Harshad Number
"""

def harshd(n):
    last_d = 0
    sum  = 0
    on = n
    while n>0:
        last_d = n%10
        sum += last_d
        n //= 10
    if sum >0 and on%sum == 0:
        return "Harshad Number"
    else:
        return "Not a Harshad Number"

num = int(input("enter your number:- "))
print(harshd(num))
