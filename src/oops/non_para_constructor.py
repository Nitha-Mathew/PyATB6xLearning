class Student:

    def __init__(self):
        self.name=input("Enter the name: ")
        self.age=input("Enter the age: ")
        self.gender=input("Enter the gender: ")
        self.place=input("Enter the place: ")

    def details(self): #self carries the instance values
        print("My name is ",self.name)

obj_stu=Student()
#obj_stu1=Student()
#obj_stu2=Student()

obj_stu.details()
#obj_stu1.details()
#obj_stu2.details()

