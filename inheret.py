class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"The full name is {self.firstname} {self.lastname}")


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)

        
