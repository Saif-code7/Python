'''## Q2. Simple Calculator
Take two numbers and an operator as input.
The operator can be:
- +
- -
- *
- /
Perform the corresponding operation and print the result.
If the user enters an invalid operator, print "Invalid Operator".
*Example:*
Enter first number: 20
Enter second number: 5
Enter operator: *
Output:
100
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator: ")
if operator == '+' :
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
else:
    print("Invalid Operator")