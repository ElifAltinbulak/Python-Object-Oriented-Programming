#VolumeCylindrical
import math
class Volume():
    def __init__(self,r,h):
        self.gr=r
        self.gh=h
    def Result(self):
        result=math.pi*(self.gr)**2*(self.gh)
        return result
    def display(self):
        print(f"Cylindrical Volume: {x.Result()}")
r = int(float(input("Yarıçap:")))
h=int(float(input("Yükseklik:")))
x = Volume(r,h)
x.display()
