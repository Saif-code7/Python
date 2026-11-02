'''**Q8. Print Squares of Numbers**

Take an integer N as input and print the square of each number from 1 to N.

Input: 5

Output: 1 4 9 16 25
'''

N = int(input("enter a number:- "))
for i in range(1,N+1,1):
    print(i*i,"",end="")