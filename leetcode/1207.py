arr = [1,2,2,1,1,3]
freq = {}
for i in arr:
    freq[i] = freq.get(i,0) + 1   # {1: 3, 2: 2, 3: 1}
print(freq)

for j,i in freq.items():
    if i == i+1 and j != j+1:
        print("False")
        break
else:
    print("True")