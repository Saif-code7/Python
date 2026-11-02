'''## Q3. Day Number

Take a number from 1 to 7 as input.

Print the corresponding day:

- 1 → Monday
- 2 → Tuesday
- 3 → Wednesday
- 4 → Thursday
- 5 → Friday
- 6 → Saturday
- 7 → Sunday

If the number is outside 1 to 7, print `"Invalid Day"`.

**Example:**Enter number: 5

Output:
Friday

'''

day = int(input("Enter number:- "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")