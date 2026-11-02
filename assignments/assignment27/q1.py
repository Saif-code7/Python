'''
Take the marks of a student as input.

Print the grade according to the following rules:

- 90 or above → "A"
- 75 to 89 → "B"
- 60 to 74 → "C"
- 40 to 59 → "D"
- Below 40 → "Fail"

*Example:*


Enter marks: 82

Output:
Grade B


'''

marks = int(input("enter marks of student :- "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")

