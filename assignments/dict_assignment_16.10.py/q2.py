"""Q2. Find the Smallest Value
Given a dictionary containing numbers, find the 
smallest value without using min().

Example:
Input: {'a': 10, 'b': 25, 'c': 5, 'd': 40}
Output: 5
"""

d = {'a': 10, 'b': 25, 'c': 5, 'd': 40}
small = d['a']
for key, elem in d.items():
    if elem < small:
        small = elem
print(small)