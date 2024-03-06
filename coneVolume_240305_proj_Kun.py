# create a Cone class
# with a constructor
# and a getVolume method

pi = 22 / 7


class Cone:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def getVolume(self):
        return 1 / 3 * self.r * self.r * pi * self.h


# test cases
a = Cone(4, 4)
print("{0:.2f}".format(a.getVolume()))

# add more test cases


a = Cone(4, 3)
print("{0:.2f}".format(a.getVolume()))
a = Cone(9, 3)
print("{0:.2f}".format(a.getVolume()))
a = Cone(1, 3)
print("{0:.2f}".format(a.getVolume()))
a = Cone(1, 5)
print("{0:.2f}".format(a.getVolume()))
a = Cone(7, 7)
print("{0:.2f}".format(a.getVolume()))
a = Cone(1.5, 3)
print("{0:.2f}".format(a.getVolume()))
a = Cone(1.5, 5)
print("{0:.2f}".format(a.getVolume()))

"""
Sample Data: 
4 4
4 3
9 3
1 3
1 5
7 7
1.5 3
1.5 5

Sample Output : 
67.02
50.27
254.47
3.14
5.24
359.19
7.07
11.78
"""
