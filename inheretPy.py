#this is a inheretance in python
#base class
class Animal:
    def eat(self):
        print("I can eat")
    
    def sleep(self):
        print("I can sleep!")

    
#derived class or obtain from the source so when you derive you'll get the functions/method of a parent class as well
class Dog(Animal):

    def bark(self):
        print("I can bark! Woof! Woof!")

#creat an object of the dog class
dog_1 = Dog()

dog_1.eat() #this will let the dog tell that it will sleep
dog_1.sleep() #this will let the dog tell that the dog will sleep
dog_1.bark() #this will let the dog tell that wants to bark



