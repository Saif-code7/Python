"""Q6. Calculate Simple Interest
Create a function simple_interest() that takes 
P, R, and T and returns the Simple Interest.

Formula:
SI = (P × R × T) / 100

Example:
Input:
P = 1000
R = 5
T = 2

Output:
100
"""
def simple_interest(P,R,T):
    return (P*R*T)/100

p = float(input("enter principal: -"))
r = float(input("enter rate of interest:- "))
t = float(input("enter time period:- "))

print(simple_interest(p,r,t))