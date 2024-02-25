class Rectangle:
    def __init__(self, a, b):
        self.width = a
        self.length = b

    def getPerimeter(self):
        return 2 * (self.length + self.width)

# Create a Rectangle class  with a constructore
# a getPerimeter method

a = Rectangle(12, 5)
print(a.getPerimeter())

a = Rectangle(131, 75)
print(a.getPerimeter())

# add more test cases
