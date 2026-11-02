"""Q5. Check Whether a Number Contains Digit 7

Take an integer N as input and check whether the digit 7 is present in the number.

Example:
Input: 58371
Output: Present
"""

n = int(input("enter your number:- "))
count  =  0
ld = 0
while n>0:
    ld = n%10
    if ld == 7:
        count += 1
        break
    n = n//10
if count >0:
    print("present")
else:
    print("not present")
