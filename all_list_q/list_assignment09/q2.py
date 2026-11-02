"""Q2. Count Positive and Negative Numbers

Create a list and count the number of positive and negative elements. Ignore zeros.

Example:

Input: [10, -5, 20, -8, 0, 7]

Output:

Positive: 3

Negative: 2
"""

arr = [10, -5, 20, -8, 0, 7]
count_p = 0
count_n = 0
for i in arr:
    if i >0:
        count_p += 1
    elif i <0:
        count_n += 1
print(f"the number of positive elements are:-  {count_p}")
print(f"the number of negative elements are:-  {count_n}")



