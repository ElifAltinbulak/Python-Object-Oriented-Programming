"""Difficulty: Intermediate
Create a new Python project with three classes plus another class to test the logic in your code. The main classes of the program are the following classes:

Person
Student
Professor
The Student and Teacher classes inherit from the Person class.

The Student class will include a public Study() method that will write I'm studying on the screen.

The Person class must have two public methods Greet() and SetAge(int age) that will assign the age of the person.

The Teacher class will include a public Explain() method that will write I'm explaining on the screen.

Also create a public method ShowAge() in the Student class that writes My age is: x years old on the screen.

You must create another test class called StudentProfessorTest with a Main method to do the following:

Create a new Person and make him say hello
Create a new Student, set an age, say hello, and display her age on the screen.
Create a new Teacher, set an age, say hello and start the explanation."""
class Person:
    def Greet(self):
        print("Hello!")
    def SetAge(self,age):
        return age
class Student(Person):
    def Study(self):
        print("I'm studying")
    def ShowAge(self):
        print(f"My age is {self.SetAge(21)} years old")
class Professor(Person):
    def Explain(self):
        print("I'm explaining")

np=Person()
ns=Student()
nt=Professor()
np.Greet()
ns.Greet()
ns.ShowAge()
ns.Study()
nt.Greet()
nt.Explain()
