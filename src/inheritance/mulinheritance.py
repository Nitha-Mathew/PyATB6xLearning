class DBBase:
    def db_connect(self):
        print("connecting to DB")

    def same(self):
        print("First")
class APIBase:
    def API_Auth(self):
        print("API Authentication")

    def same(self):
        print("Second")

class TestHybrid(APIBase, DBBase):
    def run(self):
        self.db_connect()
        self.API_Auth()
        print("Yes")
        self.same()
obj_th=TestHybrid()
obj_th.run()

