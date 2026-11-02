"""Q4. Count Occurrences of an Element

Create a list and count how many times a 
given number appears in it.

Example:

Input: [2, 4, 2, 6, 2, 8]

Number: 2

Output: 3
"""


arr = [2, 4, 2, 6, 2, 8]
target = int(input("enter your number:- "))
count_t = 0

for i in arr:
    if i == target:
        count_t += 1
print(count_t)