#input and output

  #output
 
name = "Harsh"
age = 24

#two ways of using variables inside print statement

print("hello your name is ",name,"and your age is " , age)
#formatted statement
print(f"your name is {name} and your age is {age}")


  # inputs

age = input("what is your age : ")

print(f"your age is {age}")

age = int(input("what is your age : "))    #used type conversion because 10 is int 
                                        #and to add it to age convert it to integer
#another way
# age = int(age)
print(f"your age after 10 years will be {age + 10}") #- this way also



# operators

a = int(input("enter first number"))
b = int(input("enter second number"))

print(f"your sum is {a+b}")
print(a-b)
print(a*b)
print(a/b)
print(int(a/b))   #instead this you can use -  // floor division removes all 
print(a//b)        #the values after decimal point

print(5**2)  #5 power 2
print(43%5)



#q take input of 3 num and calculate simple interest 

p = int(input("enter principal : "))
r = float(input("enter rate : "))
t = int(input("enter time : "))

si = (p*r*t)/100
print("your simple interst will be ",si)


#now calculate compound interest

p = int(input("enter principal : "))
r = float(input("enter rate : "))
t = int(input("enter time : "))

ci = (p*(1+(r/100))**t) - p
print("your compound interst will be ",ci)


# 23/09

#assignment operator - ---  =


a = 12

a = a + 10
# print(a)

count = 10
count += 1  #short hand operations -- count = count + 1

# count -= 1
# count += 1
# count *= 1
# count /= 1
# print (count)


# comparison operator

a = 45
b = 60
#(== , != , > , < , >= , <=)

# print(a > b)  #False
# print(a < b)  #f
# print(a == b) #T
# print(a != b) #F
# print(a >= b) #T
# print(a <= b) #T


#strings comarison

# print("A" > "B")
# print(ord("A"))  # to know about unicode  -- ordinal value
 
# print("BAB" > "AABCCCC")   ## COMPARES FIRST LETTER THEN MOVES NEXT
# print(ord("5"))
# print("50" > "400")   #true beacause comapres first letter

#logical operators
#(and, or , not)

print(12 == 12 , 34 != 67 )

#and operator demands only one thing that all the 
#comparisons must be true then only I will provide
#the result as true
print(12 == 12 and 34 != 67 and 34 == 34 and 50 == 50)

#or operator demands any one comparison must be true then only 
# I willprovide true
print(12 == 34 or 45 != 45 or 23 > 34 or 50 == 50)  #-- one is true

#not operator - it converts true to false and false to true

print(not 12 == 12)

print((not 12 != 12 and 45 == 45 and 23 != 23) or #first not is only for 12 != 12
      (45 > 34 or 12 == 12 or 489 > 1234))


