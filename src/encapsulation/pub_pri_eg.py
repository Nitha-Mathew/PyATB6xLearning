#private attribute
class Pwd:
    def __init__(self):
        self.password="Nitha"
        self.__password_secure="1234"   #private

    def acc(self):
        print(obj_pwd.__password_secure)

obj_pwd=Pwd()
print(obj_pwd.password)
#print(obj_pwd.__password_secure) private attribute cannot be accessed
obj_pwd.acc() #pvt attributes are encapsulated within the method(acc). It can be accessed only through the method.