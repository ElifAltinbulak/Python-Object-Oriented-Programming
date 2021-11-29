class EGO:
    def __init__(self,type,money):
        self.type=type
        self.money=money
    def work(self):
        if self.type=="öğrenci":
            if self.money>=1.75:
                self.money=self.money-1.75
                print(f"Öğrenci kalan para:{self.money}")
            elif self.money<1.75:
                print("Bakiye yok")
        elif self.type=="tam":
            if self.money>=3.25:
                self.money=self.money-3.25
                print(f"Tam kalan para:{self.money}")
            elif self.money<3.25:
                print("Bakiye yok")
        else:
            print("Error")
y1=EGO("öğrenci",50)
y2=EGO("tam",1)
y3=EGO("öğrenci",0)
y4=EGO("öğrenci",1.75)
y1.work()
y2.work()
y3.work()
y4.work()
y4.work()
