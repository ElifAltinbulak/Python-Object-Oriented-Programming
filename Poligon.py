from abc import ABC,abstractmethod
class Poligon(ABC):
    @abstractmethod
    def edge(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimater(self):
        pass
    @abstractmethod
    def show(self):
        pass
class Triangle(Poligon):
    def edge(self,a,b,c,h):
        self.a=a
        self.b=b
        self.c=c
        self.h=h
    def area(self):
        return (self.h*self.c)/2
    def perimater(self):
        return (self.a+self.b+self.c)
    def show(self):
        print(f"Area:{self.area()}\nPerimater:{self.perimater()}")
class Rectangular(Poligon):
    def edge(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def perimater(self):
        return 2*(self.a+self.b)
    def show(self):
        print(f"Area:{self.area()}\nPerimater:{self.perimater()}")
class Square(Poligon):
    def edge(self,x):
        self.x=x
    def area(self):
        return self.x**2
    def perimater(self):
        return 4*self.x
    def show(self):
        print(f"Area:{self.area()}\nPerimater:{self.perimater()}")
print("Triangle")
t1=Triangle()
t1.edge(2,3,4,5)
t1.show()
print("Rectangular")
t2=Rectangular()
t2.edge(2,4)
t2.show()
print("Square")
t3=Square()
t3.edge(2)
t3.show()
