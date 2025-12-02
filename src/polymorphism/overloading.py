#performed between methods in same class
class Person:
    def say_name(self,name): #this will not be considered, which means overloadimg does not happen
        print("I am", name)
    def say_name(self,name, last_name):
        print("I am", name, last_name)

per=Person()
per.say_name("Nitha", "Mathew")