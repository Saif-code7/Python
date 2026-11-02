'''**Q1.Weekly Attendance Analysis**

An institution records the attendance status of a student for 
**7 consecutive days**. The status is entered as P for Present and A for Absent.

Write a program to determine the **total number of days the student was present and absent**.
'''


daysPresent = 0
daysAbsent = 0
for i in range(1,8):
    a = input("enter attendance:- ")
    if a == "P":
        daysPresent += 1
    else:
        daysAbsent += 1
print(f"days present - {daysPresent}")
print(f"days absent - {daysAbsent}")

