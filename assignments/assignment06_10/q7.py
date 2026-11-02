"""Q7. Find the Largest Digit
Create a function largest_digit() that takes a 
number and returns the largest digit present in it.

Example:
Input: 58321
Output: 8
"""

def largest_digit(n):
    large = 0
    
    while n>0:
        ld = n%10
        if ld>large:
            large = ld
        
        n = n//10
    return large

num = int(input("enter a number:- "))
print(largest_digit(num))