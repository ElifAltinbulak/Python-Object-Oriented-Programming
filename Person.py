"""Difficulty: Intermediate
Create a Python program that prompts the user for three names of people and stores them in an array of Person-type objects. There will be two people of the Student type and one person of the Teacher type.

To do this, create a Person class that has a Name property of type string, a constructor that receives the name as a parameter and overrides the ToString () method.

Then create two more classes that inherit from the Person class, they will be called Student and Teacher. The Student class has a Study method that writes by console that the student is studying. The Teacher class will have an Explain method that writes to the console that the teacher is explaining. Remember to also create two constructors on the child classes that call the parent constructor of the Person class.

End the program by reading the people (the teacher and the students) and execute the Explain and Study methods."""
class Person:
    def __init__(self,name):
        self.__name=name
    def ToString(self):
        print(self.__name)
class Student(Person):
    def Study(self):
        print("the student is studying")
class Teacher(Person):
    def Explain(self):
        print("teacher is explaining")
p1=Student("Juan")
s1=Student("Sara")
t1=Teacher("Carlos")
p1.ToString()
s1.ToString()
t1.ToString()
t1.Explain()
s1.Study()
p1.Study()
