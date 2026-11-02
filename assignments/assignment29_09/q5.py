'''**Q5. Print Multiplication Table**

Take an integer N as input and print its multiplication table from 1 to 10.

Input: 3

Output:

3 6 9 12 15 18 21 24 27 30
'''

num = int(input("enter a number:- "))
for i in range(num,num*10+1,num):
    print(i,"",end="")