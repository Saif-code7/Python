#count hills and valleys in an array
nums = [2,4,1,1,6,5]
new = [nums[0]]
for i in nums:
    if new[-1] != i:     
        new.append(i)
print(new)

count = 0
for i in range(1,len(new)-1):
    if new[i-1] < new[i] > new[i+1]:
        count += 1
    elif new[i-1] > new[i] < new[i+1]:
        count += 1
print(count)