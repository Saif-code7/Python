# rotating list

"""input: [1,2,3,4,5]
k:2"""

arr = [1,2,3,4,5]
k = 2
k = k%(len(arr))

for i in range(k):
    last = arr.pop()    #dafault pop value gives last element
    arr.insert(0,last)
print(arr)
