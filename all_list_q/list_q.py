"""
# Print List Elements in Reverse Order
#
# Reverse the list using the two-pointer approach.
#
# Example:
# Input: [10, 20, 30, 40, 50]
# Output: [50, 40, 30, 20, 10]
"""
arr = [ 10,20,30,40,50]
n = len(arr)
mid = n//2

for i in range(mid):
    arr[i] , arr[n-i-1]  =  arr[n-i-1] , arr[i]    

print(arr)

"""
# Print Positive and Negative Elements of a List
#
# Print positive and negative elements separately.
# Ignore zero.
#
# Example:
# Input: [10, -5, 20, -3, 0, 8]
# Output:
# Positive: 10 20 8
# Negative: -5 -3
"""

arr = [ 10,-5,20,-3,0,8]
l_evn =[]
l_odd =[]

for i in range(0,len(arr) ):
    if arr[i]>0:
        l_evn.append(arr[i])
    elif arr[i]<0:
        l_odd.append(arr[i])

print(l_evn)
print(l_odd)


arr = [10, -5, 20, -3, 0, 8]
l1 = []
l2 = []
for i in arr:
    if i>0:
        l1.append(i)
    elif i<0:
        l2.append(i)
print(l1)
print(l2)


# other method
arr = [ 10,-5,20,-3,0,8]

print("positive: ")
for elem in arr:
    if elem>0:
        print(elem)

print("negative:- ")
for elem in arr:
    if elem<0:
        print(elem)



# Mean of List Elements
#
# Calculate the average of all elements in a list.
#
# Example:
# Input: [10, 20, 30, 40]
# Output: Mean = 25.0

ar = [10,20,30,40]
length = len(ar)
total = 0
for i in ar:
    total = total+i
print(total/length)



"""
# Find the Greatest Element and Its Index
#
# Find the greatest element and 
# print its index.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Max element = 145 
# found at 4 index
"""


arr = [2, 96, 69, 77, 145, 20]
large = arr[0]
n = len(arr)
index = 0
for i in range(n):
    if arr[i] > large:
        large = arr[i]
        index = i
print(f"Max element = {large}")
print(f"found at {index} index")


#13/10

"""
# Find the Smallest Element and Its Index
#
# Find the smallest element and print its index.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Min element = 2 found at 0 index
"""

arr = [2, 96, 69, 77, 145, 20]
min = arr[0]
index = 0
for i in range(1,len(arr)):
    if arr[i] < min:
        min = arr[i]
        index = i
print(f"Min element = {min} found at {index} index")




"""
# Find the Second Greatest Element
#
# Find the second-greatest distinct element.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Second greatest element = 96
"""

arr = [2, 96, 69, 77, 145, 20]
large = arr[0]
sl = 0
for i in range(1,len(arr)):
    if arr[i] > large:
        sl = large
        large = arr[i]
    elif arr[i] > sl and arr[i] !=large:
        sl = arr[i]
print(f"Second greatest element = {sl}")





"""
# Find the Missing Number
#
# A list contains numbers from 1 to N, but one number
# is missing. Write a program to find the missing number.
#
# Example:
# Input: [1, 2, 4, 5]
#
# Output:
# Missing Number = 3
"""

arr = [1,2,4,5]
n = len(arr)
og_n = n+1
og_sum = ((og_n)*(og_n+1)) //2
real_sum = 0
for elem in arr:
    real_sum += elem
missing = og_sum - real_sum
print(missing)



"""
# Check Whether a List Is Sorted
# Check if the list is sorted in ascending order.
# Example:
# Input: [10, 20, 30, 40, 50]
# Output: List is Sorted
"""
# my_method
arr = [10, 20, 30, 40, 50]
n = len(arr)
count = 0
for i in range(1,n):
    if arr[i] >arr[i-1]:
        count += 1
if count == n-1:
    print("list is sorted")
else:
    print("list is not sorted")

# sir_method
arr = [10, 20, 30, 40, 50]
is_sorted = True
for i in range(0,n-1):                                               # index 3 tak chalna hai kyu kee agr arr[3] > arr[4] tbhi nhi toh out of bound ho jayega
    if arr[i] > arr[i+1]:
        is_sorted = False
if is_sorted:
    print("Array is sorted")
else:
    print("Array is unsorted")




"""
# Palindromic List
#
# Check whether the list 
# reads the same from front and back.
#
# Example:
# Input: [2, 3, 15, 15, 3, 2]
# Output: Palindromic List
"""
arr = [2, 3, 15, 15, 3, 2]
n = len(arr)
is_palindrome = True

for i in range(n//2):
    if arr[i] !=arr[n-i-1]:
        is_palindrome = False
        break
if is_palindrome:
    print("palindrome")
else:
    print("not a palindrome")

# palindromic lsit or not for single elements string method
arr = [2,3,3,2]
arr2 = str(arr)
og = arr2
rev  = ""

for i in arr2:
    rev = i+ rev

if rev == og:
    print("list is palindrome")
else:
    print("list is not palindrome")

    