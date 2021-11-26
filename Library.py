class Library:
    def __init__(self,book="books",cd="cd",magazine="magazine"):
        self.book=book
        self.cd=cd
        self.__magazine=magazine
    def get(self):
        return self.__magazine
class Student(Library):
    def lib(self):
        print(f"Book:{self.book}\nCD:{self.cd}")
        
class Teacher(Library):
    def lib(self):
        print(f"Book:{self.book}\nCD:{self.cd}\nMagazine:{self.get()}")

def show():
    qu=int(input("Welcome\n1-Student\n2-Teacher\nChoose this part:"))
    if qu==1:
        print("Welcome Dear Student;")
        s1=Student()
        s1.lib()
    elif qu==2:
        print("Welcome Dear Teacher;")
        t1=Teacher()
        t1.lib()
    else:
        print("Error")
show()
