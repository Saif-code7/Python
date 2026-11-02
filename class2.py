#strings

#string has indexing it starts from 0 ang goes till the length of your word

#string also has negative indexing starting from the negative side 
#and its index are negative starting from -1

a = "1234sdgdfgsg@3#"
name = "SHERYIANS"

print(name[3] , name[0])
print(name[0],name[-1])

#string slicing - to access a part of string 

name = "SHERYIANS"  #  start:stop:steps

print(name[0:4:1])                # colon only in string slicing
print(name[::]) # default
print(name[-1:-7:-1])


# type conversion 

a = 12
a = str(a)
print(type(a), a)

a = 12 
a = float(a)
print(type(a), a)

print("7" + "3")