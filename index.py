print("Hello World!")
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