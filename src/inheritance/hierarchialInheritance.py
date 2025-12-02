class Father:
    def setup(self):
        print("I am setup")

class Child1(Father):
    def step1(self):
        print("I am step1")

class Child2(Father):
    def step2(self):
        print("I am step2")

Child1().setup()
Child1().step1()
Child2().setup()
Child2().step2()