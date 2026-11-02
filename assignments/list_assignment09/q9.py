"""Q9. Find the Largest Element

Create a list of numbers and find the 
largest element without using the max() function.

Example:

Input: [12, 45, 23, 67, 34]

Output: 67
"""
arr = [12, 45, 23, 67, 34]
large = arr[0]

for i in range(1,len(arr)):
    if arr[i] > large:
        large = arr[i]
print(large)
