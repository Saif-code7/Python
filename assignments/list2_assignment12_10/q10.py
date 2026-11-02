"""**Q10. Print Elements at Odd Indices**

Print all elements present at odd indices 
(1, 3, 5, …) of a list.

**Example:**

- Input: [10, 20, 30, 40, 50, 60]
- Output: [20, 40, 60]
"""

arr = [10, 20, 30, 40, 50, 60]
arr2 = []
for i in range(len(arr)):
    if i%2!=0:
        arr2.append(arr[i])
print(arr2)
