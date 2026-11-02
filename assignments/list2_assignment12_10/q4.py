"""**Q4. Swap First and Last Elements**

Create a list and swap its 
first and last elements.

**Example:**

- Input: [10, 20, 30, 40, 50]
- Output: [50, 20, 30, 40, 10]
"""

arr = [10, 20, 30, 40, 50]
n = len(arr)

arr[0] , arr[n-1]  =  arr[n-1] , arr[0]

print(arr)