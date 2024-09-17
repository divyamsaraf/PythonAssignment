class Shape:
    def __init__(self):
        pass
    
    def area(self):
        print("Area of Shape:", 0)

class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length
    
    def area(self):
        area = self.length ** 2
        print("Area of Square:", area)

length = float(input("Enter the length of the square: "))

shape = Shape()
shape.area()  

square = Square(length)
square.area()
