"""**Q7. Count Numbers Greater 
Than a Given Value**

Create a list and count how many 
elements are greater than a given number.

**Example:**

- Input: [10, 25, 15, 40, 30]
- Number: 20
- Output: 3
"""

arr =[10, 25, 15, 40, 30]
count = 0
number = int(input("enter your number:- "))
for i in arr:
    if i>number:
        count += 1
print(count)