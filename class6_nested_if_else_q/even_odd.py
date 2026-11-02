"""
# Q4. Number Game
#
# Take a number from the user.
# If the number is positive, 
# check whether it is even or odd.
#
# If the number is even, 
# check whether it is divisible by 4 or not.
#
# Print the appropriate result.
#
# Example:
# Enter number: 12
#
# Output:
# # Positive
# Even
# Divisible by 4
"""

num  = int(input("enter a number:- "))
if num>0:
    print(f"{num} is positive",end="")
    if num%2==0:
        print(", even ",end="")
        if num%4==0:
            print(" and divisible by 4  ")
        else:
            print(" and not div by 4")   #,end=""  for same line prnting
    else:
        print(", odd")
else:
    print(f"{num} is -")
