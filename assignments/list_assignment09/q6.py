"""Q6. Find the Second Largest Element

Create a list and find the second largest distinct element without using sort() or max().

Example:

Input: [10, 25, 15, 40, 30]

Output: 30
"""

arr = [10, 25, 15, 40, 30]
large = arr[0]
s_large = arr[1]

for i in arr:
    if i > large:
        s_large = large
        large = i

    elif i > s_large and i!= large:
        s_large = i

print(s_large)

