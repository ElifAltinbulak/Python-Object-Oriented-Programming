"""Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student  which inherits from the Person class and which also has a section attribute.
Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
Create a student object via an instantiation on the Student class and then test the displayStudent method. """
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:{self.name}\nAge:{self.age}")
class Student(Person):
    def __init__(self,name,age,section):
        super().__init__(name,age)
        self.section=section
    def displayStudent(self):
        print(f"Name:{self.name}\nAge:{self.age}\nSection:Section {self.section}")
student=Student("Name",20,1)
student.displayStudent()
