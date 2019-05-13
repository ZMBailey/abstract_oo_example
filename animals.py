from abc import ABC, abstractmethod

#The abstract class, at the most generic level of the object
class Animal(ABC):

    @abstractmethod
    def make_noise(self):
        pass

    @abstractmethod
    def move(self):
        pass

#slightly more specific
class Bird(Animal):
    def move(self):
        print("Flying!")

class Feline(Animal):
    def move(self):
        print("Silently stalk")

#the actual classes to be isntantiated
class BarredOwl(Bird):
    def make_noise(self):
        print("Hoo!")

class Mallard(Bird):
    def make_noise(self):
        print("Quack!")

class Lion(Feline):
    def make_noise(self):
        print("Roar!")

class Calico(Feline):
    def make_noise(self):
        print("Meow!")



