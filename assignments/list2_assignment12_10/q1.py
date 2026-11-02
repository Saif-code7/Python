"""**Q1. Separate Even and Odd Numbers**

Create a list of integers and separate the even and
odd numbers into two different lists.

**Example:**

- Input: [1, 2, 3, 4, 5, 6]
- Output:
    - Even: [2, 4, 6]
    - Odd: [1, 3, 5]
"""

arr = [1, 2, 3, 4, 5, 6]
l_evn = []
l_odd = []
for i in arr:
    if i %2 == 0:
        l_evn.append(i)

    else:
        l_odd.append(i)
print(f" Even : {l_evn}")
print(f" Odd : {l_odd}")