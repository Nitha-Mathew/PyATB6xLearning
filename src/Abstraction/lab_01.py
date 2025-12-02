#hiding complex functionalities while exposing only the essantial features.

from abc import ABC, abstractmethod

class Animal(ABC):  #inheritance
    def __init__(self,name):
        self.name=name

    @abstractmethod    #this means the method is incomplete
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("bark")

dog=Dog("Bruno")
dog.sound()

#the class Animal is hidden here and the method sound is completed in the class dog.


