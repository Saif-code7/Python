"""Q4. Find Maximum
Create a function maximum() that takes two 
numbers and returns the greater number.

Example:
Input: 15 25
Output: 25
"""

def maximum(a,b):
    if a>b:
        return a
    elif a == b:
        return "both numbers are equal"
    else:
        return b

x = int(input("enter first number:- "))
y = int(input("enter second number:- "))
result = maximum(x,y)
print(result)