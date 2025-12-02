#mixture of different inheritance

class Base():
    def base_mtd(self):
        print("base_mtd")

class A(Base):
    def a_mtd(self):
        print("a_mtd")

class B(Base):
    def b_mtd(self):
        print("b_mtd")

class C(A,B):
    def c_mtd(self):
        print("c_mtd")