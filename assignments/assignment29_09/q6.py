'''**Q6. Sum of First N Natural Numbers**

Take an integer N as input and calculate the sum of numbers from 1 to N.

Input: 5

Output: 15
'''

num = int(input("enter a number:- "))
sum = 0
for i in range(1,num+1,1):
    sum = sum+i
    
print(sum)