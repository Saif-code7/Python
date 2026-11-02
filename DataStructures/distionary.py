"""
DICTIONARY
1.Dictionary annoted by {curly brakets}
2.Dictionary are combination of mutiple keys:values
3.Dictionary are mutable.
4.dictionary are hetrogeneous   keys and values can have diff datatypes
5. in dist keys willl be unique but values can be dublicate.
6. dict are ordered 
"""
# d = {1:10, 2:20, 3:30}
# print(d[2])

# # 3.Dictionary are mutable.      
# d = {1:10, 2:20, 3:30}            
# d[3] = 100
# print(d)

# d = {1:10, 2:20, 3:30}
# d[4]  = 100 # creating a ney key : value that never exists

# # 5. in dist keys willl be unique but values can be dublicate.
# d = {1:10, 2:20, 3:30, 2:100}  #override ho jayegi 
# print(d)

# # 6. dict are ordered 
# d  =  {0.5:10, 2:20,3:20}      # values can be dublicate
# print(d)


# d = {1:10, 2:20, 3:30}

# for i in d: #-> 1
#     print(i,d[i]) #1.d[1]

# 16/10

#METHODS IN DICT
#1,  .keys()
d = {"ravi" : 80, "Rohan" : 23, "Devraj" : 88}
print(d.keys())

#2. .values()
print(d.values())

#3. .items() - > it gives both keys and values
print(d.items())

#4. .pop() -> key and remove both key and value and retuen the corresponding value
d.pop("Rohan")
print(d)

#5.  .get() -> agr key present hai in dict so we will get value for that key 
                #otherwise none or any message

d = {"1":10,"2":20,"3":30,"4":40}
print(d.get(5,"Not Found"))


#6.  .update()-> merge two dictionary.
a = {1:10,2:20,3:30}
b = {4:40,5:50,6:60}
a.update(b)
print(a)

"""a = {1:10,2:20,3:30}   # yhn pe override ho jayegi 3 kee value
b = {3:40,5:50,6:60}
a.update(b)
print(a)
"""


# print only keys
d  = {"Ravi": 60,"abhishek":33,"rohan" : 12}
#METHOD 1:-
print(d.keys())

#METHOD 2:-
for i in d:
    print(i)

#METHOD 3:-
for key ,value in d.items():
    print(key)


# print total marks(only)
"""d  = {"Ravi": 60,"abhishek":33,"rohan" : 12}
total = 0
for i in d:
    total += d[i]
print(total)"""

"""
# for i in d.values():
#     total = total+d[i]
# print(total)"""


"""d  = {"Ravi": 70,"abhishek":88,"rohan" : 12}
for i in d:
    if d[i] >50:
        print(i)"""

# for key in d.items():
    # if it

"""d  = {"Ravi": 70,"abhishek":88,"rohan" : 12}
large = 0
item = 0
for i in d:
    if d[i] > large:
        item = i
        large = d[i]       
print(item,large)"""


"""high = 0
top = 0
for name,marks in d.items():
    if marks > high:
        high = marks
        top = name
print(top,high)"""


d  = {"Ravi": 70,"abhishek":88,"rohan" : 12}
for i in d:
    d[i]  =  d[i]  +5
print(d )

    
