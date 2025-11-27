class Student:
    '''    name=None
    age=None
    gender=None
    place=None'''

    def __init__(self,name,age,gender,place): #This is a parameterised constructor. whenever an obj is created,
                                                # the init fn is called and self is loaded
                                                #with that instance values which can be used in all other methods.
        self.name=name
        self.age=age
        self.gender=gender
        self.place=place

    def details(self): #self carries the instance values
        print("My name is ",self.name)

obj_stu=Student("Nissy", "42", "Female", "Vellarikund")
obj_stu1=Student("Nitha", "36", "Female", "Vellarikund")
obj_stu2=Student("Sherin", "38", "Female", "Vellarikund")

obj_stu.details()
obj_stu1.details()
obj_stu2.details()

