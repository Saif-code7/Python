'''**Q7. Count Numbers from 1 to N**

Take an integer N as input and count how many numbers are present from 1 to N.

Input: 7

Output: 7
'''

# num = int(input("enter a number:- "))
# count = 0
# for i in range(1,num+1,1):
#     count = i
# print(count)
    
    
N = int(input("enter your number:- "))
count = 0
for i in range(1,N+1):
    count = count+1
print(count)
