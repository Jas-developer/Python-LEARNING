#class polymorphism
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print(f"move{self.brand}")
        
class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print(f"Move{self.brand}")
        
class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print(f"Move {self.brand}")
        

car1 = Car("Ford","Mustang")
boat1 = Boat("Ibiza","Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1,boat1,plane1):
    x.move()
    
    
#inheretance polymorphism
class Vechicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Move!")
        
class Car(Vechicle):
    pass #putting pass here because it will throw an error otherwise

class Boat(Vechicle):
    def move(self):
        print("Sail!")

class Plane(Vechicle):
    print("Fly!")
    
