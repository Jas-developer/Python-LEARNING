#PYTHON ARITHMETIC OPERATORS 
#addition 
add = 10 + 5
print(add) # result is 15
#substraction
substraction = 10 - 5
print(substraction) # result is 5
#multiplication 
multiplication = 10 * 5
print(multiplication) # result is 50
#division
division = 10 / 5
print(division) # result is 2 
#modulus
modulus = 10 % 5
print(modulus) # result is 0
#Exponentiation
exponentiaton = 10 ** 5
print(exponentiaton) # result is  
#floor division
flordiv = 10 // 5
print(flordiv) #result is  2

#python list
#list are customizable 


listSample = ["apple","banana","cheery"]
print(listSample)
#print banana
print(listSample[1])
#change banana to orange
listSample[1] = "orange"
print(listSample)
#print the length or the number amoount of the list
print(len(listSample));

# list with multiple types of different data types
multiTypes = [1,"Data", True, False, 2.0]
#printing the multi types
print(type(multiTypes))
print(type(multiTypes[4]))

#creating list constructor 
multiTypes = list(("apple","banana","orange"))
print(multiTypes)

