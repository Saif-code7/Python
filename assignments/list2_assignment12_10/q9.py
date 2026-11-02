"""**Q9. Merge Two Lists**

Merge two lists into a single list without 
using the + operator.

**Example:**

- Input: [1, 2, 3] and [4, 5, 6]
- Output: [1, 2, 3, 4, 5, 6]
"""

l1 = [1, 2, 3] 
l2 = [4, 5, 6]

l1.extend(l2)
print(l1)