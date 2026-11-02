"""Q1. Find the Smallest Element

Create a list of numbers and find the smallest element without using the min() function.

Example:

Input: [12, 5, 23, 8, 17]
"""

arr = [12, 5, 23, 8, 17]
small = arr[0]

for i in range(1,len(arr)):
    if arr[i] < small:
        small = arr[i]
print(f"the smallest number is: {small}")
