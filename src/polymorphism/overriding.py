#needs inheritance
class BaseTest:
    def run(self):
        print("test A is running")

class new(BaseTest):
    def run(self): #overriding
        print("test B is running")

obj=new()
obj.run()
