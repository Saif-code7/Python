'''**Q2. Print Numbers from N to 1**

Take an integer N as input and print numbers from N to 1.

Input: 5

Output: 5 4 3 2 1
'''

N = int(input("enter a number: - "))
for i in range(N,0,-1):
    print(i," ",end="")