"""
# Q2. Student Result
#
# A student has marks in three subjects:
# Mathematics, Science and English.

 Take the marks of all three subjects as input.

A student passes only when:
- They score at least 40 marks in every subject.

If the student passes all three subjects, print "Pass".
Otherwise, print "Fail".

Example:
Mathematics: 65
Science: 72
English: 38

Output:
Fail

"""

a = int(input("whats the marks of mahematics :- "))
b = int(input("whats the marks of science :- "))
c = int(input("whats the marks of english :- "))
if a >= 40 and b >= 40 and c >= 40:
    print("pass")
else:
    print("Fail")