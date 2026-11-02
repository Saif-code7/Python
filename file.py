"""Take a positive integer N as input and print all prime numbers from 1 to N (inclusive). 

Note: 1 is not a prime number.

**Example:** Input: 10 → Output: 2, 3, 5, 7
"""

n = int(input("enter your number:- "))

for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if i%j ==0:
            count += 1
    if count == 2:
        print(j)
        





"""Given a non-negative integer, check whether it is a Strong number. The sum of the factorials of its digits must equal the original number.

**Example:** Input: 145 → Output: Strong Number (1! + 4! + 5! = 145)
"""

# n = int(input("enter your number:- "))
# sum = 0
# 
# on =n
# while n >0:
#     fact = 1
#     ld = n%10
#     for i in range(1,ld+1):
#         fact = fact*i
#     sum = sum + fact
#     n = n//10
# if sum == on:
#     print("strong number")
# else:
#     print("not a strong number")


"""Given a non-negative integer, check whether it is an Armstrong number. Raise each digit to the power equal to the number of digits, then check whether the sum equals the original number.

**Example:** Input: 153 → Output: Armstrong Number (1³ + 5³ + 3³ = 153)
"""

# n = int(input("enter youyr number:- "))
# sum = 0
# length = len(str(n))
# on = n
# while n>0:
#     ld = n%10
#     sum = sum + (ld**length)
#     n = n//10
# if sum == on:
#     print("Armstrong number")
# else:
#     print("not")




"""Take an integer N as input and find the second largest distinct digits present in the number.

Example: Input: 58382

Output: Second Largest: 5

 Check Palindrome Number
"""

# n = int(input("enter your number:"))
# large = 0
# sl = 0
# while n>0:
#     ld = n%10
#     if ld > large:
#         sl = large
#         large = ld
#     elif ld > sl and ld != large:
#         sl = ld
#     n = n//10
# print(sl)        





"""#### 5. Check palindrome number (10 marks)

        Take an integer N as input and check whether              the number remains the same when its digits               are reversed.

      Example:
      Input: 121

      Output : Palindrome
"""

# n =int(input("enter your number:- "))
# on = n
# s = 0
# while n>0:
#     ld = n%10
#     s = s*10+ld
#     n = n//10
# if s == on:
#     print("palindrome")

# else:
#     print("not")
