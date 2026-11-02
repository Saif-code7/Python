"""Q8. Check Voting Eligibility
Create a function eligible() that 
takes age as an argument.
If age is 18 or above, return "Eligible", otherwise 
return "Not Eligible".

Example:
Input: 20
Output: Eligible
"""

def eligible(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"

age = int(input("enter the age:- "))
print(eligible(age))