"""**Q8. Count Numbers Smaller Than a Given Value**

Create a list and count how many elements are 
smaller than a given number.

**Example:**

- Input: [10, 25, 15, 40, 30]
- Number: 20
- Output: 2
"""

arr = [10, 25, 15, 40, 30]
number = int(input("enter your number:- "))
count = 0
for i in arr:
    if i<number:
        count+= 1
print(count)