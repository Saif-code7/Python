"""Q9. Check Armstrong Number
Create a function is_armstrong() that takes a number and 
checks whether it is an Armstrong number.

Example:
Input: 153
Output: Armstrong
"""

def is_armstrong(n):
    length = len(str(n))
    sum = 0
    ld = 0
    on = n
    while n>0:
        ld = n%10
        sum = sum+ (ld**length)
        n = n//10
    if sum == on:
        print("Armstrong number")
    else:
        print("not an armstrong number")

num = int(input("enter your number:- "))
is_armstrong(num)