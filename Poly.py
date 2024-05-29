class Polygon:
    #method to render a shape
    def render(self):
        print("Rendering polygon")

class Square(Polygon):
    #renders Square
    def render(self):
        print("Rendering Circle")

class Circle(Polygon):
    #renders circle
    def render(self):
        print("Rendiring Circle..")
        
s_1 =Square()
s_1.render()