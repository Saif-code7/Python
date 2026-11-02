# Q8. Print All Numbers Ending with 7 from 1 to N
#
# Take an integer N as input and 
# print all numbers from 1 to N that end with the digit 7.
#
# Example:
# Input: 40
# Output:
# 7 17 27 37
"""
# write a function of this code and return me list
# return 
# list [] 
# append -
"""

# using list
def nums_ending_with_7(num):
    result = []
    for i in range (1,num+1):
        if i%10 == 7:
            result.append(i)
    return result

n = int(input("enter your number:- "))
ans = nums_ending_with_7(n)
print(ans)

"""def nums_ending_with_7(n):
    for i in range(1,n+1):
        ld = i%10
        if ld == 7:   # if i%10 == 7
            print(i)


n = int(input("enter your number:- "))

nums_ending_with_7(n)"""
