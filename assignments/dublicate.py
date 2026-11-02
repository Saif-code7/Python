"""remove dublicate elements from the given list
ex = 
input: [1, 2, 3, 2, 4, 1, 5]
output: [1,2]
"""
arr = [1, 2, 3, 2, 4, 1, 5]
n = len(arr)
l2 = []
for i in range(n):
    count = 1         # count ko 1 hee rkhenge kyu kee already ek element hai toh count 1
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            count += 1
    if count > 1:
        l2.append(arr[i])
print(l2)


"""i current element select karta hai.
j uske baad ke elements ko ek-ek karke check karta hai.
Inner loop khatam hone ke baad hi outer loop ka i aage badhta hai"""