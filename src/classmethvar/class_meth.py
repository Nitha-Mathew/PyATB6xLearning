class Car:
    base_rate=10000 #class variable
    def __init__(self,door,window,gear):
        self.door=door
        self.window=window
        self.gear=gear

    def base_rate_calc(self):
        print("Rate is", self.base_rate)

    @classmethod #for updation of class variable and can call other class methods,
                #cannot access or modify instance variables directly
    def base_rate_updation(Cls): #class is its first argument
        base_rate=Cls.base_rate+(.1*Cls.base_rate)
        print(base_rate)

Car.base_rate_updation() #no object creation