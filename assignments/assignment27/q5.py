'''## Q5. Triangle Type

Take three sides of a triangle as input.

Check the type of triangle:

- If all three sides are equal → `"Equilateral"`
- If any two sides are equal → `"Isosceles"`
- If all three sides are different → `"Scalene"`

**Example:**
Enter side 1: 5
Enter side 2: 5
Enter side 3: 7

Output:
Isosceles
'''
a = int(input("Enter side :- "))
b = int(input("Enter side :- "))
c = int(input("Enter side :- "))

if a == b and b == c and a == c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")