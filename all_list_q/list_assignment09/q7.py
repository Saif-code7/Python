"""Q7. Replace Negative Numbers with Zero

Create a list and replace every 
negative element with 0.

Example:

Input: [10, -5, 20, -8, 7]

Output: [10, 0, 20, 0, 7]
"""

arr = [10, -5, 20, -8, 7]
l2 =[]

for i in arr:
    if i <0:
        i = 0
    l2.append(i)
print(l2)



"""for i in range(0,len(arr)):
    if arr[i] <0:
        arr[i] = 0
print(arr)
"""
        