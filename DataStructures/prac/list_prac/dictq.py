# print unique elements in an array

"""a = [1,1,2,3,4,2,2,3,3,4,7,7,7,7,5,5]

d = {}
for i in a:
    if i in d.keys():
        d[i] += 1          # freq concept 
    else:
        d[i] = 1

print(d.keys())"""


# count frequency of array elements 

"""a = [1,1,2,3,4,2,2,3,3,4,7,7,7,7,5,5]

freq =  {}
for i in a:
    freq[i] = freq.get(i,0) + 1

print(freq)
"""

"""s1 = "aabbcc"
s2 = "baccab"

d = {}
for i in s1:
    d[i] = d.get(i,0)+1

for i in s2:
    if i in d.keys():
        d[i] -= 1 

    else:
        print("an extra element was found ")

for i in d:
    if d[i] != 0:
        print("sorry your elements are not same")
        break
else:
    print("your strings are same")"""

#print elements occuring twice
"""a = [1,1,2,2,5,5,5,6,6,1,2,3,4,5,6,7,8,9,0]
d = {}
for i in a:
    d[i] = d.get(i,0) + 1

ans = []
for i in d:
    if d[i] > 1:
        ans.append(i)

print(ans)"""

# nums = [0,1,2,2,4,4,1]
# d = {}
# for i in nums:
#     d[i] = d.get(i,0)+1

# for i in d%2 == 0:
#     print(i)

a = [1,2,2,1]
b = [2,2]
j = []
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

# for i in b:
#     if i in d.keys():
#         print(i)
#         break

for i in d.keys():
    if i in b:
        j.append(i)

print(j)
