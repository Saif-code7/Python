"""
Question: Merge Two Sorted Lists Without Using sort()
Write a Python program to merge two sorted lists into a single
sorted list without using the sort() function or any Sorting Algo.
Example:
Input:
arr1 = [1, 4, 7, 10]
arr2 = [2, 3, 8, 9]

Output:
[1, 2, 3, 4, 7, 8, 9, 10]
"""

arr1 = [1,4,7,10]
arr2 = [2,3,8,9]
n1 = len(arr1)
n2 = len(arr2)
l2 = []

i = 0
j = 0
while i < n1 and j < n2:
    if arr1[i] < arr2[j]:
        l2.append(arr1[i])
        i += 1
    else:
        l2.append(arr2[j])
        j += 1

# this part for last element kyu kee wo kissse compare 
# hoga or agr compare nhi hoga toh list me kaise aayeg
while i < n1:
    l2.append(arr1[i])
    i += 1

while j < n2:
    l2.append(arr2[j])
    j += 1

print(l2)


# arr1 = [1, 4, 7, 10]
# arr2 = [2, 3, 8, 9]
# n = len(arr1)
# m = len(arr2)
# ans = []
# i = 0
# j =0

# while i < n and j <m:
#     if arr1[i] < arr2[j] :
#         ans.append(arr1[i])
#         i += 1
#     else:
#         ans.append(arr2[j])
#         j += 1

# while i< n :
#     ans.append(arr1[i])
#     i += 1
# while j <m :
#     ans.append(arr2[j])
#     j += 1
# print(ans)

