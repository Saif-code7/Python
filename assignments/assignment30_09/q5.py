'''**Q5. Attendance Eligibility**

A student has **10 classes**. For every class, enter P for Present and A for Absent.

Calculate the students **attendance percentage** and display whether the student has **75% or more attendance**.
'''

percent = 0
TotalDays = 0
for i in range(1,11):
    attendance = input("enter attendance:-  ")
    if attendance == "P":
        TotalDays += 1
percent = (TotalDays/10)*100     # yhn pe maine percent loop ke andar nikala tha jo glt output 
print(f"Attendance percentage = {percent}")  #nhi deta but outside loop is the more preferred way
if percent >= 75:
    print("yes more than 75%")