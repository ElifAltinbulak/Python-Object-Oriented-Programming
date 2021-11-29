class Fraction:
    def __init__(self,nr,dr=1):
        self.nr=nr
        self.dr=dr
        self.new_nr=0
        self.new_dr=0
        if self.nr<0 and self.dr<0:
            self.new_nr=-1*(self.nr)
            self.new_dr=-1*(self.dr)
        elif self.dr<0:
            self.new_nr=-1*(self.nr)
            self.new_dr=-1*(self.dr)
        else:
            self.new_nr=self.nr
            self.new_dr=self.dr
    def show(self):
        print(f"{self.new_nr}/{self.new_dr}")
    def multiply(self,other):
        if isinstance(other,int):
            other=Fraction(other)
        return Fraction(self.new_nr*other.new_nr,self.new_dr*other.new_dr)
    def add(self,other):
        if isinstance(other,int):
            other=Fraction(other)
        return Fraction(((self.new_nr*other.new_dr)+(other.new_nr*self.new_dr)),(self.new_dr*other.new_dr))
f1=Fraction(2,3)
f1.show()
f2=Fraction(3,4)
f2.show()
f3=f1.multiply(f2)
f3.show()
f3=f1.add(f2)
f3.show()
f3=f1.add(5)
f3.show()
f3=f1.multiply(5)
f3.show()
