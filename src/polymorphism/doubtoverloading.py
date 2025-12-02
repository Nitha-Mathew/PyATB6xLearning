class BaseTest:
    def addition(self,a,b):
        print(a+b)
    def addition(self,*a):
        sum=0
        for i in a:
            sum=sum+i
        print(sum)

obj=BaseTest()
obj.addition(5,9)

