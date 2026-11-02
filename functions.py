#functions - are block of codes that can be reused again and again

# how functions are created
# inbuild
"""
print()
input
range
str()
len()
"""

# user defined functions -

#defining a function
# def hello():
#     print("how are you")          # bina call kiye yeh kaam nhi krega

# #calling a function
# hello()

# # return

# def hey():
#     return "how are you"   #return the value to 
#                            #the calling block

# a = hey() # calling block captures the value      agr sirf hey() likhte toh bas call hota kuch hota nahi
# print(a)



#parameters and arguments

# def addition(a,b):  #you accept the parameters
#     print(a+b)

# addition(10,20) #and you provide the
#                 #arguments to the parameters
# addition(50,50)   # function ko baar baar call kr skte h


#        #OR

# def addition(a,b):  #you accept the parameters
#     return(a+b)

# print(addition(10,20)) #and you provide the
#                 #arguments to the parameters
# print(addition(50,50))   



#        #OR

# def addition(a,b):  #you accept the parameters
#     print(a+b)

# x = addition(10,20) #and you provide the
#                 #arguments to the parameters
# y = addition(50,50)   
# print(x)
# print(y)
 


# def palindrome(n):
        
#     ld = 0
#     s=0

#     temp = n
#     while n>0:
#         ld = n%10
#         s = s*10+ld
#         n = n//10
#     # print(s)

#     if s == temp:
#         print("palindrome number")
#     else:
#         print("not a palindrome number")

# palindrome(121)
# b = 343
# palindrome(b)


# 06/10

# types of parameters and arguments

"""# default parameters
when you assign

def hello(a,b,c,d,e = 30):    # agr ek baar pehle default parameter de diye toh baad me nhi de 
    print(a + b)              # payenge it follws positional arguments exception - range()

hello(50,50,20,56)

# default arguments

def information(name,age,number):
    print(name)
    print(age)
    print(number)

information(number = 9907554321,name = "harsh, age = 25")
information"""


"""# print nos from 1 to 30
# you cannot use for and while loop
# you cannot uses print statement more than 1"""

                       #RECURSION       ->  has a range of 999
                       # a function calling itself
"""
def numbers(n):       # function creation
    if n == 30:       # base case 
        return
    print(n)
    numbers(n+1)      # function calling

numbers(1) """


def hello1():
    hello2
    print("hello1")

def hello2():
    hello3
    print("hello2")

def hello3():                      # stack last in first out pehle 4,3,2,1
    hello4                          # agr kisi karan se (function call) ke wajah se 
    print("hello3")                 #baki ka code exwcute nhi hota h toh woh stack k anadar chala jata h

def hello4():
    print("hello4")

hello1()


def numbers(n):
    if n == 31:
        return
    numbers(n+1)
    print(n)          # yhn pe bhi stack reverse me no print hoga

numbers(1)