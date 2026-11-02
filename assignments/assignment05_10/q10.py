"""Q10. Count Digits
Create a function count_digits() that takes 
a number and returns the total number of digits.

Example:
Input: 12345
Output: 5
"""

def count_digits(n):
    count = 0
    while n!=0:
        count += 1
        n = n//10
    return count

num = int(input("enter your number:- "))
print(count_digits(num))