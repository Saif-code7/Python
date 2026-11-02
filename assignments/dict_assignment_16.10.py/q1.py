"""Q1. Find the Largest Value
Given a dictionary containing numbers, find the 
largest value without using max().

Example:
Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
Output: 40
"""
d = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
large = d['a']
for i in d:
    if d[i] > large:
        large = d[i]
print(large)


d = {'a': 10, 'b': 25, 'c': 40, 'd': 15}
large = 0
index = 0
for key , num in d.items():
    if num > large:
        index = key
        large = num
print(index,large)