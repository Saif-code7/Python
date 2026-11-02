"""
# Q4. Sum of Odd Numbers from 1 to N
#
# Take an integer N as 
# input and calculate the sum of all odd numbers from 1 to N.
#
# Example:
# Input: 10
# Output: 25
# (Explanation: 1 + 3 + 5 + 7 + 9 = 25)
"""

# sum = 0
# for i  in range(1,n+1):
#     if i%2 !=0:
#         sum +=i
# print(sum)

# using functions:-
def sum(n):
    add =0
    for i in range(1,n+1):
        if i%2!=0:
            add += i
    return add

n  = int(input("enter  a number:- "))

print (sum(n))
 