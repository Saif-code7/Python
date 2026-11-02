"""Q2. Check Prime Number
Create a function is_prime() that takes a number and returns 
"Prime" if the number is prime, otherwise returns "Not Prime".

Example:
Input: 17
Output: Prime
"""

def is_prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        return "prime"
    else:
        return"Not Prime"

n = int(input("enter a number:- "))
print(is_prime(n))
