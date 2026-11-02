"""
TUPLE
1. Annoted by (paranthesis)
2. tuples are ordered.
3. tuples are immutable.
4. tuples can store duplicate values
5. tuples are hetrogeneous
"""

# # t = () empty tuple
# t = (1,2,3,4)
# # t[2] = 100 # not possible
# print(t[2])
# t = (1,2,3,4,1,2,3,"hello",True , 7.32)
# print(t)



"""METHODS IN TUPLE
1.  .INDEX() -> RETURN index of any value
2.  .count() -> count occurence of any value
"""

# t = (1,2,3,4,2)
# print(t.index(2))
# print(t.count(2))


"""# operation 
+ -> concatenation   #line 36
* - > repetition  # line 37
"""

# t1 = (1,2)
# t2 = (3,4)
# print(t1 + t2)
# print(t1 * 5)


# add 100 at last
t = (1,2,[3,4,5])
# print(t[2].append(100))  # tuple is a class so nhi hoga directly print se
t[2].append(100)
print(t)


t = (1,2,3,4,5,6,7,8)
print(t[1:6])

t = (1,2,3,4,5,6,7,8)
print(t[::-1])

# t = (1,2,3,4,5,6,7,8)
print((1,2)* 2 + (3,))