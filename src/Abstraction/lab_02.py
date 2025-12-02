from abc import ABC, abstractmethod
class Father(ABC): #inherits abstract class
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def loan(self):
        pass

class Son(Father):
    def loan(self):
        print("Paying the loan")

amit=Son("Singh")
amit.loan()

#here abstract class has the actual loan holder which is hidden in abstract class.
