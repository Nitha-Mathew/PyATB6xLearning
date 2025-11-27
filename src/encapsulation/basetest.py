class BaseTest:
    _driver="chrome"

    def setup(self):
        print("Launching Browser :", self._driver)

    def teardown(self):
        print("closing browser")

class LoginTest(BaseTest):
    __username="admin"
    __password="1234"

    def getUser(self):
        user=self.__username
        return user

    def runtest(self):
        print("Running login test with user: ",self.getUser())

obj_base=BaseTest()
obj_login=LoginTest()
obj_base.setup()
obj_login.runtest()
obj_base.teardown()
