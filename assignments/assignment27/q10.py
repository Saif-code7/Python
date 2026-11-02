'''## Q10. Exam Eligibility

Take a student's attendance percentage and marks as input.

A student is eligible to appear for the final exam only if:

- Attendance is **75% or above**
- Marks are **40 or above**

If both conditions are satisfied, print `"Eligible"`.

Otherwise, print `"Not Eligible"`.

**Example:**Enter attendance: 82
Enter marks: 55

Output:
Eligible
'''
attendance = float(input("Enter aattendance: "))
marks = float(input("Enter marks"))

if attendance >= 75 and marks >= 40:
    print("Eligible")
else:
    print("Not Eligible")
