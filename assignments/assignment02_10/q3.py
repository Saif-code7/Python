"""Q3. Find the Smallest Number

Take N numbers as input and determine the smallest number among them.

Example:
Input:
5
18
7
25
3
12

Output:
3
"""

N = int(input("enter your number:- "))
num = int(input("enter number:- "))
for i in range(1,N):
    n = int(input("enter number:- "))
    if n<num:
        num = n
print(f"the smallest number is :- {num}")