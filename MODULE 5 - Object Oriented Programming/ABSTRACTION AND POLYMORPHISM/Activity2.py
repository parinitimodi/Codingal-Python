from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move (self):
        print("I can speak")
class Dog(Animal):
    def move (self):
        print("I can bark")
R = Human()
R.move()         
K = Dog()
K.move()