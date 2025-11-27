class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b


    def sum(self):
        res=self.a+self.b
        print (res)

    def mul(self):
        res=self.a*self.b
        print (res)

cal=Calc(8,8)
cal1=Calc(5,9)
cal.sum()
cal1.mul()



