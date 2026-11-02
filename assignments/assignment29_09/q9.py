'''**Q9. Sum of Even Numbers**

Take an integer N as input and calculate the sum of all even numbers from 1 to N.

Input: 10

Output: 30
'''

num = int(input("enter your number:- "))
sum = 0
for i in range(1,num+1):
    if i%2 == 0:
        sum = sum+i

print(sum)
