'''**Q4. Print Odd Numbers**

Take an integer N as input and print all odd numbers from 1 to N.

Input: 10

Output: 1 3 5 7 9
'''

N = int(input("enter a number:- "))
for i in range(1,N+1,2):
    print(i,"",end="")
