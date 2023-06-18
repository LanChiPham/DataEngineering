# 1. creating class
class myClass:
    x = 5 

# access class member
print ("access class member")
myObj = myClass()
print (myObj.x)


# 2. class __init__ function 
print ("class with __init__ function")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.nationality = "Vietnamese"

    def printValues(self):
        print (f"Name: {self.name}")
        print (f"Age: {self.age}")
        print (f"nationality : {self.nationality}")

objPerson = Person("John", 25)
print ("Class with init function. name = {0} , age = {1}, nationality = {2}".format(objPerson.name, objPerson.age, objPerson.nationality))
objPerson.printValues()

# modify object 
objPerson.age = 40

# delete object properties 
del objPerson.age 

# delete object 
del objPerson

# pass statement 