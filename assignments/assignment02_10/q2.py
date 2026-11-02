"""Q2. Difference Between Largest and Smallest
+Take N numbers as input and calculate the difference between the largest and smallest number.
Example:
Input:
5
10
25            
7
18
12
Output:
22
"""


n = int(input("enter your number:- "))
small = int(input("enter expected number:-"))
large = small
for i in range(n-1):
    num = int(input("enter your numbers_ "))
    if num > large:
        large = num
    elif num < small:
        small = num
print(large)
print(small)
print(large - small)



# for positive integers only
n = int(input("enter your number:- "))
small = int(input("enter expected number:-"))
large = 0
for i in range(n-1):
    num = int(input("enter your numbers_ "))
    if num > large:
        large = num
    elif num < small:
        small = num
print(large)
print(small)
print(large - small)