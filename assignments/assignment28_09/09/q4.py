'''**Q4. Number Comparison**
Take two numbers as input. First check whether both numbers are equal.
If not equal, check which number is greater.
Input: 10, 20
Output: Second Number is Greater
'''
a = int(input("enter first number:- "))
b = int(input("enter second number:- "))

if a==b:
    print("BOTH NUMBERS ARE EQUAL")
else:
    if a>b:
        print("First Number is Greater")
    else:
        print("Second Number is Greater")

