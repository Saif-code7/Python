'''## Q4. Divisibility Checker

Take an integer as input.

Check whether the number is:

- Divisible by both 3 and 5
- Divisible only by 3
- Divisible only by 5
- Not divisible by either 3 or 5

Print the appropriate message.

**Example:**
Enter number: 15

Output:
Divisible by both 3 and 5
'''

num = int(input("Enter a number:- "))
if num%3 == 0 and num % 5 == 0 :
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible only by 3")
elif num % 5 == 0:
    print("Divisible only by 5")
else :
    print("Not divisible by either 3 or 5")