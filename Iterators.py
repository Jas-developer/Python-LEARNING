list = iter(["Jason","Ken","Hazel","Rojon","Lorna","Kate"])

#looping through a list
print(next(list))

#learning iter & next 
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 1
            return  x
        else:
            raise StopIteration
    
    
myClass = MyNumbers()
myiter  =  iter(myClass)
#we will put a limmit to our iterator loop

#stoping the function
#so this will now work you have to stop it from the next method itself otherwise it will result to infinite loop
for x in myiter:
        print(x)