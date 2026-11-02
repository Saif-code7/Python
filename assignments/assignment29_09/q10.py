'''**Q10. Print Multiples of 5**

Take an integer N as input and print the first N multiples of 5.

Input: 5

Output: 5 10 15 20 25
'''

N = int(input("tell your number:- "))
for i in range(1,N+1):
    print(5*i,"",end="")