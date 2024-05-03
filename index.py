
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

