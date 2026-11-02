"""Q4. Count Numbers Having Digit 0

Take N integers as input and count how many of them contain the digit 0.

Example:
Input:
5
10
25
30
17
40

Output:
3
"""

N = int(input("enter the number for range:- "))
count= 0
for i in range(1,N+1):
    n = input("enter the number:- ")

    if "0" in n:
        count += 1
print(count)                        