"""Q6.Update All Values
Increase every value in a dictionary by 5.

Example:
Input: {'a': 10, 'b': 20, 'c': 30}
Output: {'a': 15, 'b': 25, 'c': 35}
"""
d = {'a': 10, 'b': 20, 'c': 30}
for i in d:
    d[i] += 5 
print(d)


{'a': 10, 'b': 20, 'c': 30}
for i in d.values():
    i += 5
print(d)