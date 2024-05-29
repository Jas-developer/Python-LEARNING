x = lambda a : a + 10 #lambda is equavalent to arrow function in javascript
print(x(45))

#CREATE A PARROT CLASS
class Parrot:
    name = ""
    age = 0

#create parrot1 object
parrot1 = Parrot()
parrot1.name = "Tedy"
parrot1.age = 21

#create parrot 2 with parrot class
parrot2 = Parrot()
parrot2.name ="Bear"
parrot2.age =12

#access the attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")

#python inheretance
#Use of the inheretance in python

