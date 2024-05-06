#parent class
class Parent: #this is the parent class
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
       fullname = f"My name is {self. firstname} {self.lastname}"
       print(fullname)
       
class Child(Parent):
    def __init__(self, fname, lname,age,location):
        super().__init__(fname, lname)
        self.age = age
        self.location= location
        
x = Child("Jason","Evaristo",21,"Davao City")
#printing the child object that inhereted the properties of a parent class
print(x.location)