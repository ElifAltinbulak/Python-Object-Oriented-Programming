"""Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
    def init(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r
2 - Define a Area() method of the class which calculates the area of ​​the circle.
3 - Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
4 - Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not."""
class Circle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.r=self.b-self.a
    def Area(self):
        return self.r**2*3.14
    def Perimeter(self):
        return 2*3.14*self.r
    def testBelongs(self):
        print(f"a:{self.a}\nb:{self.b}\nr:{self.r}\nArea:{self.Area()}\nPerimeter:{self.Perimeter()}")
circleC=Circle(2,3)
circleC.testBelongs()
C=Circle(0,3)
C.testBelongs()
