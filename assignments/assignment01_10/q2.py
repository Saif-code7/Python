'''Q2. Find the Largest Among N Numbers

Take N numbers as input and determine the largest number among them.

Example:
Input:
5
10                                # very very imp q can be done without arrays think!!!!!
25
7
18
12

Output:
25
'''

N = int(input("enter the number:- "))
num = int(input("enter your number:- "))
for i in range(1,N):
    n = int(input("enter number:- "))
    if n > num:
        num = n
        
print(num)
    
