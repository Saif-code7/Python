"""Q5. Print Elements at Even Indices

Create a list and print the elements 
present at even indices (0, 2, 4, …).

Example:

Input: [10, 20, 30, 40, 50, 60]

Output: [10, 30, 50]
"""

arr = [10, 20, 30, 40, 50, 60]
l2 =[]
for i in range(0,len(arr)):
    if i%2 ==0:
        l2.append(arr[i])
print(l2)
