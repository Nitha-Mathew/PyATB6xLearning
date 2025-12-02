#no object creation for calling staticmethod.
#practically usd in excelread....
#more faster
#no self or cls
#cannot access or modify class variables ,instance variables or other methods
#purpose: utility functions, helper functions
#they take some parameters and work on that parameters.

class Person:
    def details(self,name):
        print("Name of the person is ",name)
    @staticmethod
    def salary(base):
        salary=base+.1*base
        print(salary)

Person.salary(10000)