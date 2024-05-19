#learning OOP in python
class MyFirstClass: #this is my first class in python
    x = 5


#my first class with init constructor
class Person:
    def __init__(self,name,age,work,gender):
        self.name = name
        self.age = age
        self.work = work
        self.gender = gender

personA = Person("Jameson", 56, "Inigat","Bayot Gyud")

employeeA = f"{personA.name} is a {personA.age} years old {personA.work} and he is {personA.gender}"
print(employeeA)

#class with str function
class PersonStr:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is a {self.age} years old  Developer"
    #creating object methods
    def PersonName(self):
        print(f"The name of the person is: {self.name}")
    
p1 = PersonStr("James",25) #the str function/method manipulate the data that should be return by the class
#print(p1)

p1.PersonName()