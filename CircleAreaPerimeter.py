#CircleAreaPerimeterOOP3
import math
class Cırcle():
    def __init__(self,r):
        self.gr=r
    def Area(self):
        area=math.pi*(self.gr)**2
        return area
    def Perimeter(self):
        perimeter=2*math.pi*(self.gr)#yukarda yazdığını kullanmak için self kullanmak lazım
        return perimeter
    def display(self):
        print(f"Area Result: {result.Area()}\nPerimeter Result: {result.Perimeter()}")
        
a=int(input("Please Circle radius: "))
result=Cırcle(a)
result.display()
