class BaseTest:
    def test1(self):
        print("This is test 1")

class UITest(BaseTest):
    def test2(self):
        print("This is test 2")

class APITest(UITest):
    def test3(self):
        self.test1()
        #self.test2()
        print("This is test 3")

obj_test=APITest()
obj_test.test3()

