'''**Q1. Print Numbers from 1 to N**

Take an integer N as input and print all numbers from 1 to N.

Input: 5

Output: 1 2 3 4 5 '''

N = int(input("enter number:- "))
for i in range(1,N+1,1):
    print(i," ",end="")