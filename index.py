
#learning lambda 4/30/24
fullName = lambda firstNAme,lastName : firstNAme + " "+ lastName
print(fullName("Jason", "Evaristo"))
#using lambda inside the function
def myFunc(n):
    return lambda a:a * n

myDoubler = myFunc(5)#this will return a lambda that contain functionalities that i can use


print(myDoubler(2))
#we will create a function that will multiply the arguments of function into 3
def timesThree(num):
    return lambda param:param*num


multiThree = timesThree(100)
printThis = multiThree(3)
#I am expecting this function to return 300
print(printThis)


#LEARNING PYTHON ARRAYS
#array are used to store multiple values in one single variable
cars = ["Ford","Volvo","MBW"]

cars.append("Honda")

for x in cars:
    if(x == "Volvo"):
        x = "Kawasaki"
        cars.append("Yamaha")
        

def returnAllData():
    data = []
    for x  in cars:
        data.append(x)
    return data

#extract the data from the function
for x in returnAllData():
    print(x)
    
testName = ["Jason","John Doe","Manny"] #this is a list/array of s trings#
#append method
testName.append("Floyd")
print(testName)

for x in testName:
    if(x == "Floyd"):
        continue
    print(x)
    
#clear method
testName.clear()
#printing the names


#OOP In python
#Object oriented programming
#creating an object with  class in python


class myFullName:
    firstName = "Jason"
    lastName =  "Evaristo"
    dream = "Data Engineer"
    
p1 = myFullName();
firstName = p1.firstName
lastName = p1.lastName

fullName = f"My fullName is {firstName} {lastName} and I want to be a {p1.dream}"
#labeler
print("Currently Learning OOP in python")
print(fullName)

#using init in a class
class personInformation:
    def __init__(self,name,age,location,school,course,goal):
        #created a constructor
        self.name = name
        self.age = age
        self.location = location
        self.school = school
        self.course = course
        self.goal = goal
        
        
#creating an object 
information = personInformation("Jason Evaristo",22,"Davao City","Interface Computer College","Computer Science","Data Engineer")
#storing the object into list/array
informationList =[information.name, information.age, 
                  information.location,information.school,information.course,
                  information.goal]

informationObject = {
    "name":information.name,
    "age":information.age,
    "location":information.location,
    "school":information.school,
    "course":information.course,
    "goal":information.goal
}
#printing all the experment i made

print(informationList) #printhing the array i made
print(informationObject)#printing the object i made

#looping the information list

for x in informationList:
    print(x)
    
#5/5/24
#learning will start now
#LEARNING OBJECTS

#learning the constructor again in python 
class Person:
    def __init__(self,name,age):
        self.fullName = name
        self.myAge = age
        
    def fulllName(name):
        return f"Hello My Name is {name}"
        
    def __str__(self):
        if(len(self.fullName) >= 5 and self.myAge is not None):
            return f"Hello my Name is {self. fullName} and I'm {self.myAge} years of age"
        else:
            return 'Please provide a proper name'
        
        
personA = Person("Jaso", 22)
#printing my information as a person
print(Person.fulllName("Jason Evaristo"))



#learning Inheritance
class PersonInformation:#parent class
    def __init__(self, fname, lname):
         self.firstname = fname
         self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)
        
x = PersonInformation("Jason","Evaristo")
x.printname()

#send the parent class a paremeter to be inheret by another class
class Student(PersonInformation):#child class
    def __init__(self, fname, lname):
        super().__init__(fname,lname)#to inheret all the methods and properties of the parent class
        self.graduationyear = 2019
            
class Location(PersonInformation):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    
    def Location(place):
        return f"at {place}"
    
    
person = Location("Jason","Evaristo").Location("Davao City")