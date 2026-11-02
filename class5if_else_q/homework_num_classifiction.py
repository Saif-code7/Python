"""
# Q5 Homework. Number Classification
#
# Take an integer from the user.
#
# Your program should check the number and print:
#
# "Positive Even"      if the number is positive and even.
# "Positive Odd"       if the number is positive and odd.
# "Negative Even"      if the number is negative and even.
# "Negative Odd"       if the number is negative and odd.
# "Zero"               if the number is zero.
#
# Example:
# Enter number: -7
#
# Output:
# Negative Odd
"""

a = int(input("enter an interger :- "))
if a > 0 and a%2 ==0:
    print("positive even")
elif a>0 and a%2 != 0:
    print("positive odd")
elif a<0 and a%2 == 0:
    print("negative even")
elif a<0 and a%2 != 0:
    print("negative odd")
else:
    print("zero")