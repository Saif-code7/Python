#print sum and averge
"""a = [10,20,30,40,50]
t = 0
for i in a:
    t += i
print(f"sum is :- {t} and average is :- {t//(len(a))}")
"""

# max element with index
# a = [1,45,23,89,45,90,12,36,82]
"""a = [-10, -5, -20, -2]
index = 0
large = float("-inf")

for i in range(len(a)):
    if a[i]>large:
        large = a[i]
        index = i

print(f"largest element is:- {large} at index - {index}")"""

#second greatest element
"""a = [1,45,23,89,45,90,12,36,82]
index = 0
index2 = 0
large = a[0]
sl = a[0]
for i in range(len(a)):
    if a[i] > large:
        sl = large
        large = a[i]
        index2 = index
        index = i
        
        
    elif a[i] > sl and a[i] != large:       # agr second largest list me large k baad hai toh??
        sl = a[i]
        index2 = i 
print(f"second largest element is:- {sl} at index - {index}")"""


# check wheather list is sorted or not
"""
a = [10,20,30,40,50]
is_sort = True
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        is_sort = False

if is_sort:
    print("sorted")
else:
    print("not sorted")
"""

# method- 2
"""a = [10,20,90,40,50]
for i in range(len(a) - 1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")"""

# left rotation by 1

"""a = [10,20,30,40,50,60]
k = 1
k = k%(len(a))
for i in range(k):
    first = a.pop(0)
    a.insert(len(a),first)

print(a)"""
    
# method - 2

"""a = [10,20,30,40,50,60]
for i in range(len(a)-1):
    a[i] , a[i+1] = a[i+1] , a[i]
print(a)"""


# left rotation by k times
"""a = [10,20,30,40,50,60]
k = int(input("how many times you want to rotate: -"))
k = k%(len(a))
for i in range(k):
    for i in range(len(a) - 1):
        a[i] , a[i+1] = a[i+1] , a[i]

print(a)"""

# reverse a list without using extra space (not using empty list)
"""
a = [10,20,30,40,50,60]
n = len(a)
m = n//2
for i in range(m):
    a[i] , a[n-i-1] = a[n-i-1] , a[i]

print(a)
"""

# method -2
"""a = [10,20,30,40,50,60]
b = len(a) - 1

for i in range(len(a)//2):
    a[i] , a[b] = a[b] , a[i]
    b = b - 1

print(a)"""
    
# linear search
"""
a = [23,67,123,1,54,7,98,45,23,13,6,68]

target = 6
for i in range(len(a)):
    if a[i] == target:
        print(f"target found at {i}")
        break
else:
    print("no scuh element exists")"""


# binary search

"""def search(a,target):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start +end)//2

        if target == a[mid]:
            return mid
        elif target > a[mid]:
            start = mid + 1
        elif target < a[mid]:
            end = mid - 1

    return "no such element is present"


a = [23,67,123,1,54,7,98,45,23,13,6,68]
a = sorted(a)

target = 100
ans = search(a,target)
print(ans)"""

# bubble sort
# a = [23,67,123,1,54,7,98,45,23,13,6,68]
# for i in range(len(a)-1):
#     if a[i] > a[i+1]:
#         a[i] , a[i+1] = a[i+1] ,a[1]
# print(a)


"""a = [1,2,3,4,5,6]
num = 6
n = (num+1)//2
l1 = []
l2 = []
for i in range(n):
    l1.append(a[i])
for i in range(n,len(a)):
    l2.append(a[i])

print(l1)
print(l2)"""

# bubble sort:-
"""a = [56,234,23,24,46,334,9,52,12,3,13,644]

for i in range(len(a) - 1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]
print(a)"""