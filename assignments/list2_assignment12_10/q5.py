"""**Q5. Find the Second Smallest Element**

Find the second smallest distinct element 
without using sort() or min().

**Example:**

- Input: [15, 5, 20, 8, 12]
- Output: 8
"""

arr = [15, 5, 20, 8, 12]
small = arr[0]   
sl = float('inf')                                                    

for i in range(1,len(arr)):
    if arr[i] < small:
        sl = small
        small = arr[i]
    elif arr[i] < sl and arr[i] != small:
        sl = arr[i]
print(sl)