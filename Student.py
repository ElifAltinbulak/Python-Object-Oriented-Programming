class Student:
    def info(self,stunum):
        self.__name="name"
        self.__surname="surname"
        self.__stunum="no"
        self.__phonenum="phono"
        self.__dateofbirth="birth time"
    def get_info(self):
        return f"Name:{self.__name}\nSurname:{self.__surname}\nStudent ID:{self.__stunum}\nPhone Number:{self.__phonenum}\nDate of birth:{self.__dateofbirth}"
class Semester1(Student):
    dict1={"Math":"AA",
           "Phy":"BB"}
class Semester2(Student):
    dict2={"Math":"AA",
           "Phy":"BA"}
def gets(stunum,semester):
    stu=Student()
    stu.info("190444064")
    print(stu.get_info())
    if semester=="1":
        stus=Semester1()
        print(stus.dict1)
    elif semester=="2":
        stus=Semester2()
        print(stus.dict2)
gets("no",1)
