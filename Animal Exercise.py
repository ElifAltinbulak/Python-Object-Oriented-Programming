class Animal:
    def __init__(self,name,habitat_area):
        self.__name=name
        self.habitat_area=habitat_area
        self.sound="..."
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name=new_name
    def get_habitat_area(self):
        return self.habitat_area
    def set_habitat_area(self,new_area):
        self.habitat_area=new_area
    def vocalize(self):
        print(self.sound)
    #special method

    def __eq__(self,other):
        return self.get_name()==other.name
    def __str__(self):
        return f"Animal Name:{self.get_name()}"
class Cow(Animal):
    def __init__(self,name,habitat_area):
        super().__init__(name,habitat_area)
        self.sound="moo"
class Chicken(Animal):
    def __init__(self,name,habitat_area):
        super().__init__(name,habitat_area)
        self.sound="buck buck"
class Pig(Animal):
    def __init__(self,name,habitat_area):
        super().__init__(name,habitat_area)
        self.sound="oink"
        

c1=Chicken("chicken1","village1")
print(c1.sound)
print(c1.get_name())
print(c1.get_habitat_area())
c1.set_name("chicken2")
c1.set_habitat_area("village2")
print(c1.get_name())
print(c1.get_habitat_area())
c1.vocalize()
print(c1)

co1=Cow("cow1","village1")
print(co1.sound)
print(co1.get_name())
print(co1.get_habitat_area())
co1.set_name("cow2")
co1.set_habitat_area("village2")
print(co1.get_name())
print(co1.get_habitat_area())
co1.vocalize()
print(co1)


p1=Pig("pig1","village1")
print(p1.sound)
print(p1.get_name())
print(p1.get_habitat_area())
p1.set_name("pig2")
p1.set_habitat_area("village2")
print(p1.get_name())
print(p1.get_habitat_area())
p1.vocalize()
print(p1)
