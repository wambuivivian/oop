class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.142

    def area(self):
        return self.pi*self.radius**2
circle = Circle(5)
print("area:", circle.area())    


