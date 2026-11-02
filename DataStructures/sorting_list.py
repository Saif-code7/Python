#bubble sort

# arr = [64,34,25,12,22,11,9]
# n = len(arr)
# for i in range(n):                                     # n times lagenge sort hone mein
#     for j in range(n-i-1):                             # har baar bigger value last mee aajaat hai toh usse kam part tak iterate krenge
#         if arr[j] > arr[j+1]:                          # n - i - 2 tak chalega toh n-i-2+1 tak lenge kyu kee ek kam chalta hai
#             arr[j] , arr[j+1] = arr[j+1] , arr[j]
# print(arr)


# selection sort - arraya me smallest element khojo first ement k saath swap kr do
arr = [64, 34, 25, 12, 22, 11, 9]

n = len(arr)

for i in range(n):
    small = i

    for j in range(i + 1, n):
        if arr[j] < arr[small]:
            small = j

    arr[i], arr[small] = arr[small], arr[i]

print(arr)




