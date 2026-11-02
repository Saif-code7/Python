"""
# Q. Digit Frequency

# Take an integer N as input and count how many times
# each digit from 0 to 9 occurs in the number.
#
# Example:
# Input: 122333
#
# Output:
# 1 -> 1
# 2 -> 2
# 3 -> 3
"""


n = int(input("enter your number:- "))

for digit in range (0,10):
    count = 0
    temp = n
    while temp>0:  #12244
        ld = temp%10 #0
        if ld == digit:
            count += 1    #1
        temp = temp//10
    if count>0:
        print(f"{digit} = {count}")