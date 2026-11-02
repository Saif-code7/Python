"""
SETS
1. -> sets are annoted by {}  or set()
2. -> set stores only unique elements and remove duplicate ones
3. -> sets are unordered  does not have index -> means cannot access elements in set
4. -> sets are hetrogeneous
5, -> sets are semi-Mutable(can add or remove elemets using methods)
"""
"""s = {}
# s = set() #EMPTY SET
s = {1,1,2,2,3,4,5, 70.2,"Sample"}  # repeated values wont be counted
print(type(s))
print(s)"""


#LIST TO SET
l = [1,2,3,2,4,5]
# print(set(l))

"""
SET METHODS.
"""
#1.  .add() -> adds an element to set
"""s = {1,2,3,4}
s.add(5)
print(s)"""

#2.   .remove() -> remove an element if the element
                #    didn't exists we will get an keyerror
# s.remove(100)
# print(s)


#3.  .discard() -> will not show any error if the element is not present in set.
"""s.discard(100)
print(s)
"""



"""
SET OPERATIONS. 
"""


s1 = {1,2,3,4}
s2 = {4,5,6,7,8}
"""# 1,  .union()
merge both the sets"""

print(f"union-> {s1.union(s2)}")
print(f"union -> {s1 | s2}") # - same work without using  .union()

"""
2. .intersection
common elements.
"""

s1 = {1,2,3,4}
s2 = {4,5,6,7,8}
print(f"intersection-> {s1.intersection(s2)}")
print(f"intersection -> {s1 & s2}") 


"""
3. .difference()
elements present in one set but not in another
"""
s1 = {1,2,3,4}
s2 = {4,5,6,7,8}
print(f"Difference   {s1.difference(s2)}")
print(f"Difference   {s2.difference(s1)}")
print(f"difference -> {s1 - s2}") 

"""
4.  .symmetric_difference() 
"""

s1 = {1,2,3,4}
s2 = {4,5,6,7,8}
print(f"symmetric - {s1.symmetric_difference(s2)}")
print(f"symmetric -> {s1 ^ s2}") 


"""
| -> union
& -> intersection
- -> difference
^ -> symmetric diifference
"""


"""
frozenset makes any set with of fixed elements 
we cannot add elements or cannot remove it
"""
s = frozenset([1,2,3,4,5])   #- list dena padega forzen k lia but wo set hee hai dict se pass nhi kr skte
s.add(6)
print(s)