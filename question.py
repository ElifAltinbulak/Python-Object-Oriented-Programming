class Quadrilateral:
    def __init__(self,x,y,z,d):
        self.x=x
        self.y=y
        self.z=z
        self.d=d
class Trapezoid(Quadrilateral):
    def __init__(self,x,y,z,d):
        super().__init__(x,y,z,d)
    def Area(self):
        print(f"Area: {((self.x+self.y)/2)*self.z}")
    def Point(self):
        self.d=0
        print(f"Point(tbase,bbase,height,0):{self.x,self.y,self.z,self.d}")
class Parallelogram(Quadrilateral):
    def __init__(self,x,y,z,d):
        super().__init__(x,y,z,d)
    def Area(self):
        print(f"Area: {(self.x)*(self.z)} or {(self.y)*(self.z)}")
    def Point(self):
        self.d=0
        print(f"Point(base1,base2,height,0): {self.x,self.y,self.z,self.d}")
class Rectangle(Quadrilateral):
    def __init__(self,x,y,z,d):
        super().__init__(x,y,z,d)
    def Area(self):
        print(f"Area: {(self.x)*(self.y)}")
    def Point(self):
        self.d=0
        self.z=0
        print(f"Point(sedge,ledge): {self.x,self.y,self.z,self.d}")
class Square(Quadrilateral):
    def __init__(self,x,y=0,z=0,d=0):
        super().__init__(x,y,z,d)
    def Area(self):
        print(f"Area: {self.x**2}")
    def Point(self):
        self.y=0
        self.d=0
        self.z=0
        print(f"Point(edge): {self.x,self.y,self.z,self.d}")
a=Trapezoid(1,2,3,4)
a.Area()
a.Point()

b=Parallelogram(1,2,3,4)
b.Area()
b.Point()

c=Rectangle(1,2,3,4)
c.Area()
c.Point()

d=Square(1,2,3,4)
d.Area()
d.Point()
