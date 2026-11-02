"""Q5. Check Palindrome Number
Create a function is_palindrome() that takes a number 
and checks whether it is a palindrome.

Example:
Input: 1221
Output: Palindrome
"""

def is_palindrome(n):
    ld = 0
    s = 0
    on = n
    while n!=0:
        ld = n%10
        s = s*10+ld
        n = n//10
    if s == on:
        print("Palindrome")
    else:
        print("not a Palindrome")

num = int(input("enter your number:- "))
is_palindrome(num)
