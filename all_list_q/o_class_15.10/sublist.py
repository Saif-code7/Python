
"""
Question: Check Whether a List Is a Sublist of Another List

Write a Python program to check whether all elements of one list
appear consecutively in another list.

Example:
Input:
arr = [10, 20, 30, 40, 50]
sub = [20, 30, 40]

Output:
Sublist Found
"""
arr = [10, 20, 30, 40, 50]
n = len(arr)
sub = [20, 30, 40]
m = len(sub)

for i in range(n-m+1):
    if arr[i:i+m] == sub:
        print("Sublist Found")
        break
else:
    print("Sublist not found") 


