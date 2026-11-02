'''Q5. Print Numbers Divisible by 10

Take an integer N as input and print all the numbers from 1 to N that are divisible by 10.

Example:
Input: 50

Output:
10
20
30
40
50
'''
N = int(input("enter your number:- "))
for i in range(1,N+1):
    if i%10 == 0:
        print(i)