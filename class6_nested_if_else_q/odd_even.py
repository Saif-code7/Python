
"""
# Q2. Number Check
#
# Take a number from the user.
# If the number is even,
# check whether it is divisible by 4.
# If the number is odd, print "Odd Number".
"""

num = int(input("enter a number:- "))

if num%2 == 0:
    print(f"{num } is even ")
    if num%4==0:
        print("and divisible by 4 ")
    else:
        print("and not divisible by 4 ")
else:
    print(f"{num} is odd  ")