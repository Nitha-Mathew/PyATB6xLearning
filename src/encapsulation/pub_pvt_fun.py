#private function

class Persons:
    def __init__(self):
        self.__pvt_var="private"
        self.public="public"
        self._protected="protected" #can be accessed. but not recommended

    def mom(self): #public function
        print("mom can be accessed")
        self.__wife() #private function can be called inside the class but not outside the class
        print(self.__pvt_var)

    def __wife(self):#private function
        print("wife cannot be accessed")

obj_per=Persons()
obj_per.mom()# can be accessed
print(obj_per._protected) #don't use
# obj_per.__wife() cannot be accessed
