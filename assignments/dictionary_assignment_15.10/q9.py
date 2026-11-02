"""**Q9. Count Key-Value Pairs**

Count the total number of key-value pairs in a dictionary without using len().

**Example:**

- Input: {'a': 10, 'b': 20, 'c': 30}
- Output: 3
"""
d = {'a': 10, 'b': 20, 'c': 30}
count = 0
for i in d:
    count += 1
print(count)