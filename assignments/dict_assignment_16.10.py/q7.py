"""Q7.Count Values Greater Than a Number
Count how many dictionary values are greater 
than a given number.

Example:
Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
Number: 20
Output: 2
"""

d = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
number = int(input("enter your number:- "))
count = 0

for i in d.values():
    if i > number:
        count += 1
print(count)
