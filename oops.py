#3. object oriented approach.(classes, objects)
"""
class -> just a blueprint (attribute/method)
object -> Instance of the class
"""
"""
class Animal:
    a = "Lion" #attribute

    def hello(self): #method   self is object 
        print("this is hello function")"""

# Animal.hello() # abhi memory save nhi ho rhi h after 
# creating object class is saved in  memory

"""obj = Animal() # class initialize (creating object of the class) bina call kiye function run ho jayega just intiliasation se
obj1 = Animal()   

obj1.hello()
print(obj.a)"""

# class Vehicle:
#     def show(self):
#         print("this is show method")

#     def __init__(self): # Dunder method  constructor
#         print("this is constructor")  # pehle constructor hee chalge chahe pehel kuch bhi ho or do constructs toh overwrite hoga latest wala cha;ega
                                        # jaise hee class ka object bnega construcor run hoga and it will ask for some
                                        # inputs and if not given the code will not work
# obj = Vehicle() 
# obj.show()
"""
class vehicle:    # class declaration
    def __init__(self,color, price,fuel_type):
        self.color = color
        self.price = price         # attributes created by objects and not class
        self.fuel_type = fuel_type

        print(self.color,self.price,self.fuel_type)

obj = vehicle("Red" , "10lkh" , "CNG")"""  # class initialisation


# 17/11
# attributes and methods
"""class vehicle:    
    name = "Rohan" #class attribute
    def __init__(self,name,color):
        self.name = name  # Instance attribute(object,self,instance)
        self.color = color

        print(self.name,self.color)

    def greet(self):  #instance method cannot run without object (self)
        print("this is greet method")


    @staticmethod    # nichle wale function ko object ee koi need nhi hai run hone k lia..
    def show():   # static method will run without object (self)
        print("this is show method")
        

car1 = vehicle("BMW","Black")
car1.show()"""

class Student:
    age = 21

    @classmethod   # jo sirf class k andar kaam krega
    def show(cls): # here cls = Student   
        print(cls.age)

obj = Student()
obj.show()


class Student:
    school = "DPS"

    @classmethod   
    def show(cls,new_school): 
        cls.school = new_school
        print(cls.school)

s1 = Student()
s2 = Student()
# s1.show()
s2.show("kv")









# here cls = Student   jo class method hai wo use aata hai for globally change in every object  actual aatribute me permanent change kr deta hai





