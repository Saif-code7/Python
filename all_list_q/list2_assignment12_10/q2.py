"""**Q2. Remove Duplicates**

Create a list and remove duplicate
elements without using set().

**Example:**

- Input: [1, 2, 3, 2, 4, 1, 5]
- Output: [1, 2, 3, 4, 5]
"""

arr = [1, 2, 3, 2, 4, 1, 5]
n = len(arr)
arr2 = []
for i in range(n):
    if arr[i] not in arr2:
        arr2.append(arr[i])
print(arr2)









# ye approch yaad rkhna not in wla new list banao phir agr elemn nhi h new list me append simple