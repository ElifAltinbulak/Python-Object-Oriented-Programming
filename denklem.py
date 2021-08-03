class denklem():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def denklemsistem(self):
        return f"{self.a}x²+{self.b}x+{self.c}"
    def tepenoktası(self):
        return f"Tepe Noktası: {-self.b/(2*self.a)}"
    def delta(self):
        delta= self.b**2-4*self.a*self.c
        return delta
    def kokler(self):
        x1=(-self.b+(self.delta())**0.5)/2*self.a
        x2=(-self.b-(self.delta())**0.5)/2*self.a
        return f"""x1= {int(x1)}
x2= {int(x2)}"""
e=denklem(1,4,-12)
print(e.denklemsistem())
print(e.tepenoktası()) 
print(e.delta())
print(e.kokler())
