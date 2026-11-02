"""Q10. Find the Second Largest Digit
Create a function second_largest_digit() that takes 
a number and returns the second largest digit present in it.

Example:
Input: 58321
Output: 5
"""

# def second_largest_digit(n):
#     large = 0
#     second_l = 0

#     while n>0:
#         ld = n%10
#         if ld > large:
#             second_l = large
#             large = ld

#         elif ld > second_l and ld != large:
#             second_l = ld
#         n = n//10
#     return second_l

# num = int(input("enter your number:- "))

# print(second_largest_digit(num))



num = int(input("enter your number:- "))
large = 0
sl=0

while num>0:    #58321
    ld = num%10     #1
    if ld >large:
        sl = large  #0
        large  = ld  #1
    
    elif ld > sl and ld != large:   
        sl = ld
    num =num //10

print(sl)
