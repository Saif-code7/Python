"""**Q10. Calculate the Sum of Values**

Calculate the sum of all numerical values in a dictionary using a loop.

**Example:**

- Input: {'a': 10, 'b': 20, 'c': 30}
- Output: 60
"""

d = {'a': 10, 'b': 20, 'c': 30, }
total = 0
for i in d:
    total += d[i]
print(total)






#  agr dict me str value ho then kaise add hone dict value ->using isinstance()

d = {'a': 10, 'b': 20, 'c': 30, 'd': 'saif' }
total = 0
for i in d:
    if isinstance(d[i] , (int,float)):
        total += d[i]
print(total)