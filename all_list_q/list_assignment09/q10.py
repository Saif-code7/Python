"""Q10. Reverse a List

Create a list and reverse its elements 
without using the reverse() method.

Example:

Input: [10, 20, 30, 40, 50]

Output: [50, 40, 30, 20, 10]
"""

arr = [10, 20, 30, 40, 50]

l2 = []

for i in range(len(arr)-1,-1,-1):
    l2.append(arr[i])
print(l2)




