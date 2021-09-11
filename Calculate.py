class Calculate():
    #init metodu
    def __init__(self,num1,num2):
        #içine yazılan örnekler attribute
        self.num1=num1
        self.num2=num2
    def add(self):
        return f"Result: {self.num1+self.num2}"
    def subtract(self):
        return f"Result: {self.num1-self.num2}"
    def multply(self):
        return f"Result: {self.num1 * self.num2}"
    def divide(self):
        return f"Result: {self.num1/self.num2}"
    def exe(self):
        return f"Result: {self.num1**self.num2}"
c1=Calculate(10,5)
print(c1.add())
print(c1.subtract())
print(c1.multply())
print(c1.divide())
print(c1.exe())
sayı1=int(input("Sayı 1:"))
sayı2=int(input("Sayı 2:"))
c2=Calculate(sayı1,sayı2)
toplama=c2.add()
çıkarma=c2.subtract()
çarpma=c2.multply()
bölme=c2.divide()
üstalma=c2.exe()
print(f"""Sonuçlar:
      Toplama:{toplama},
      Çıkarma:{çıkarma},
      Çarpma:{çarpma},
      Bölme:{bölme},
      ÜstAlma:{üstalma}""")
