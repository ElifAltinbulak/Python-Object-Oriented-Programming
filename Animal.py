"""Create a Python program that implements an abstract class Animal that has a Name property of type text and three methods SetName (string name), GetName and Eat. The Eat method will be an abstract method of type void.

You will also need to create a Dog class that implements the above Animal class and the Eat method that says the dog is Eating.

To test the program ask the user for a dog name and create a new Dog type object from the Main of the program, give the Dog object a name, and then execute the GetName and Eat methods."""

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def SetName(self,name):
        pass
    @abstractmethod
    def GetName(self):
        pass
    @abstractmethod
    def Eat(self):
        pass
class Dog(Animal):
    def SetName(self,name):
        self.__name=name
    def GetName(self):
        return self.__name
    def Eat(self):
        print("dog is eating")
    def Sound(self):
        print("Havhav")
class Cat(Animal):
    def SetName(self,name):
        self.__name=name
    def GetName(self):
        return self.__name
    def Eat(self):
        print("cat is eating")
d1=Dog()
d1.SetName("Tobby")
d1.Sound()
c1=Cat()
c1.SetName("Miya")
print(d1.GetName())
print(c1.GetName())
c1.Eat()
d1.Eat()
