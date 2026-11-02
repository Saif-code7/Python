"""
Data types:
1. Numbers(int,float, complex)
2. Strings ("abc)
3. Boolean(True , False (0,1))

"""

# Data Structures -ek data ko ek structured way me rkhna
"""
list  - keeping everything in one bag in structured way

1. Square Brackets -> List[]
2. list is hetrogeneous data structure - 
   (a list can store different data types together)   # ex in line 24
3. list allows storing dublicate values  # ex in line 33
4. list are ordered - because they have indexing
   and indexing starts from 0.  jaise banayi h waisi print hogi
5. lists are mutable - we can change any value anytime and anywhere.  #ex in line 35
"""

"""marks = []   # list h kyu kee sq bracket h list is empty   empty list

marks = [80,78,90,65,88,87,75, "Abhishek" , 3.14, True, +1j]
        # 0  1  2  3  4  5 6 - index
print(marks)

print (marks[3])
print(marks[1:6])   # slicing"""


"""
marks = [80,78,80,90,"Sheryins",3.14]

marks[3] = "modiji"
print(marks[3])
print(marks)"""

#Traversing - hum list k har ek element pe jaa rhe h or print kr rhe h

# a = "Sheryians"

# for ch in a:     
#     print(ch)      aisa same kaam list me hota h

# a = [10,20,30,40,50]

# """for i in a:
#     print(i)"""

# input()
# int()
# print()
# """agr kisi keyword k aage "." nahi laga that is a function 
# lekin agr "." dot lga h toh METHOD hai """  # aise hee methods lists me aati h


# #methods in list
#1.  .append()  add the value at the last 
#  ek baar me ek value ko daal skte h

"""marks = [10,20,50,60,98]

marks.append(90)
marks.append("Saif")   # can store any value"""



# 2.  .extend()  - multiple values
# marks2 = [70,80,90]
# marks.extend(marks2)
# marks2.extend(marks)
# print(marks2)
# print(marks)



# 3.  .insert(index, value)
"""marks .insert(3,88)
print(marks)  # non existing value me bhi kaam krta h

marks.insert(5,100)
print(marks)"""

# 09/10

# #4.  .remove() -> remove any value from the list only the first occurence 
# a = [10,20,30,40,10,50]
# a.remove(10)
# print(a)

# #5.  .pop() -> emove any value basis on the index.
# a = [10,20,30,40,10,50]
# a.pop(3)     # agr index na de toh dafault last value (here 50 ) remove kr deta hai
# print(a)


# #6.  .clear() -> removes every element and gives empty list.
# a = [10,20,30,40,10,50]
# a.clear
# print(a)

# #7.  del -> removes list from the memory  - del is not a method its a keyword
# a = [10,20,30,40,10,50]
# del a
# print(a)


"""
Shallow copy
"""

# a = [1,2,3,4,5]
# b = a.copy()   #deep copy
# b[3] = 100
# print(a)
# print(b)

# l = [10,20,30,40,50,60,70,80]

# for i in l:            # for values to print use list
#     print(i)

# l = [10,20,30,40,50,60,70,80]
# for i in range(len(l)):  # for index to print use range
#     print(i, l[i])     # l is list first index pe gye or 10 print kiya

# l = [10,20,30,40,50,60,70,80]
# for i in range(len(l)-1,-1,-1):
#    print(i , l[i])


#  create an another list and store the reverse value
l = [10,20,30,40,50,60,70,80]
l2 =[]
for i in range(len(l)-1,-1,-1):
   l2 = l[i]
   print(l2)

#used append method
l = [10,20,30,40,50,60,70,80]
l2 = []

for i in range(len(l) - 1,-1,-1):
    l2.append(l[i])
print(l2)
    
