"""**Q3. Find the Index of an Element**

Create a list and find the index of a given 
element without using the index() method.

**Example:**

- Input: [10, 20, 30, 40, 50]
- Element: 30
- Output: 2
"""

arr = [10, 20, 30, 40, 50]
element = 30
index = 0
for i in range(len(arr)):
    if arr[i] == element:
        index = i
        break
print(index)
