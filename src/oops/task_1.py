
class Person:
    name=None
    age=None
    gender=None
    place=None
    phone=None

    def __init__(self,name,age,gender,place,phone):
        self.name=name
        self.age=age
        self.gender=gender
        self.place=place
        self.phone=phone

    def sing(self):
        print(f'I am {self.name}, {self.age} years of age and I am a {self.gender}. I belong to {self.place}. You can contact me at {self.phone}')

    def dance(self):
        print(
            f'I am {self.name}, {self.age} years of age and I am a {self.gender}. I belong to {self.place}. You can contact me at {self.phone}')

    def paint(self):
        print(
            f'I am {self.name}, {self.age} years of age and I am a {self.gender}. I belong to {self.place}. You can contact me at {self.phone}')

    def sports(self):
        print(
            f'I am {self.name}, {self.age} years of age and I am a {self.gender}. I belong to {self.place}. You can contact me at {self.phone}')

    def craft(self):
        print(
            f'I am {self.name}, {self.age} years of age and I am a {self.gender}. I belong to {self.place}. You can contact me at {self.phone}')


obj_stu=Person("Nissy", "42", "Female", "Vellarikund","980976")
#obj_stu1=Person("Nitha", "36", "Female", "Vellarikund")
#obj_stu2=Person("Sherin", "38", "Female", "Vellarikund")

obj_stu.craft()
#obj_stu1.details()
#obj_stu2.details()

