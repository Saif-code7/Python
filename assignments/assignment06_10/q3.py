"""Q3. Sum of Digits
Create a function sum_of_digits() that takes a 
number and returns the sum of its digits.

Example:
Input: 12345
Output: 15
"""

def sum_of_digits(n):
    sum = 0
    while n>0:
        ld = n%10
        sum = sum+ld
        n = n//10
    return sum

num =int(input("enter your number:- "))
print(sum_of_digits(num))