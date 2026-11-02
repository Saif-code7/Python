'''**Q3. Print Even Numbers**

Take an integer N as input and print all even numbers from 1 to N.

Input: 10

Output: 2 4 6 8 10
'''

N = int(input("enter a number:- "))
for i in range(2,N+1,2):
    print(i,"",end="")
