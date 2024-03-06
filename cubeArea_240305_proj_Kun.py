# create a Cube Class
# with a constructor
# and a getArea method


class Cube:
    def __init__(self, side):
        self.side = side

    def getArea(self):
        return self.side * self.side * 6.0


# test cases
# add more test cases

a = Cube(112)
print("Cube area is :: {0:.1f}".format(a.getArea()))
a = Cube(4)
print("Cube area is :: {0:.1f}".format(a.getArea()))
a = Cube(33)
print("Cube area is :: {0:.1f}".format(a.getArea()))
a = Cube(50)
print("Cube area is :: {0:.1f}".format(a.getArea()))
a = Cube(5)
print("Cube area is :: {0:.1f}".format(a.getArea()))
a = Cube(19)
print("Cube area is :: {0:.1f}".format(a.getArea()))
a = Cube(111)
print("Cube area is :: {0:.1f}".format(a.getArea()))


"""
Sample Data: 
112
4
33
50
5
19
111

Sample Output : 
Cube area is :: 75264.0
Cube area is :: 96.0
Cube area is :: 6534.0
Cube area is :: 15000.0
Cube area is :: 150.0
Cube area is :: 2166.0
Cube area is :: 73926.0

"""
