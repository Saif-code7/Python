"""Q9. Check Whether All Digits Are Even

Take an integer N as input and check whether 
every digit of the number is even.

Example:
Input: 2486
Output: Yes
"""

n = int(input("enter your number:- "))  # 2468
length = len(str(n)) #4
count =0 
while n>0:
    l = n%10    #8  6   4 2
    if l%2 == 0:
        count += 1        #1  2  3 4
    n=n//10 #2
if count == length:
    print("yes")
else:
    print("no")
        