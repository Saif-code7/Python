"""Q4.Sum of Even Values
Find the sum of all even values present in 
a dictionary.

Example:
Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}
Output: 30
"""

d = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
total = 0
for i in d:
    if d[i] %2 == 0:
        total += d[i]
print(total)