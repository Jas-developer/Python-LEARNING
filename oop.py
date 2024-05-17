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

personA = Person("James", 21, "Accountant","Bayot")

employeeA = f"{personA.name} is a {personA.age} years old {personA.work} and he is {personA.gender}"
print(employeeA)