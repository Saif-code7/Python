"""
# Q5. Number Comparison
#
# Take two numbers from the user.
#
# If the first number 
# is greater than the second number,
# check whether the first number is even or odd.
#
# Otherwise, check whether 
# the second number is even or odd.
#
# Example:
# Enter first number: 15
# Enter second number: 10
#
# Output:
# First number is greater
# First number is odd
"""




a = int(input("enter first number:- "))
b = int(input("enter sec number:- "))
if a>b:
    print(f"{a} is greater than{ b} ",end="")
    if a%2==0:
        print("and even")
    else:
        print("and odd")
else:
    print(f"{b} is greater than {a} ",end="")
    if b%2==0:
            print("and even")
    else:
            print("and odd")
    

