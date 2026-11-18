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


#  method 2 

a = [10,20,30,40,50,60]
k = int(input("how many times you want to rotate: -"))
k = k%(len(a))
for i in range(k):
    for i in range(len(a) - 1):
        a[i] , a[i+1] = a[i+1] , a[i]

print(a)