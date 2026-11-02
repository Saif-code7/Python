"""Q8. Find the Second Largest Digit

Take an integer N as input and find the second largest digit present in N.

Example:
Input: 5832
Output: 5
"""

n = 5832
large = 0
sl = 0
while n>0:
    ld = n%10
    if ld > large :
        sl = large
        large = ld
    elif ld>sl and ld != large:
        sl = ld
    n = n//10
print(sl)
