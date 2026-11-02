"""
# Q5. Print Fibonacci Series up to N Terms
#
# Take an integer N as input and print the first N terms of the Fibonacci series.
# In Fibonacci series, each number is
# the sum of the previous two numbers (starts with 0, 1).
#
# Example:
# Input: 6
# Output:
# 0 1 1 2 3 5
"""

n = int(input("enter the number "))
a = 0
b =1

for i in range(n):
    print(a , end =" ")
    c = a+b
    a =b
    b =c
 

n  =int(input("enter a number:- "))
a = 0
b = 1

# count = 2
for i in range(n):
    print(a)
    c = a+b
    a = b
    b = c
    
    
    

    
    