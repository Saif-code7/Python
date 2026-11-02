"""Q5. Count Numbers Ending with 5

Take an integer N as input and count how many numbers from 1 to N end with the digit 5.

Example:
Input: 30
Output: 3
"""

N = int(input("enter your number:- "))
count = 0
for i in range(1,N+1):
    if i%10 == 5:                #i%10 == 0 -> means number ends with 0  
        count += 1
print(count)
