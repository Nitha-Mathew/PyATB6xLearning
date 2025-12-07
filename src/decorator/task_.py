

def student_details(func): #This is the decorator function


    def address():
        func()
        print("Kaithakulam House")
        print("Vellarikund")
        print("Kasaragod")
        print("Kerala")
    address()


@student_details
def name_1(): #some details needs to be added to this function. The extra details added in a decorator
    print("Student name is Nitha MAthew")
    print("Age is 36")
@student_details
def name_2():#some details needs to be added to this function
    print("Student name is Nissy MAthew")
    print("Age is 42")
@student_details
def name_3():#some details needs to be added to this function
    print("Student name is Sherin MAthew")
    print("Age is 38")
