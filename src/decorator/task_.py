

def student_details(func):


    def address():
        func()
        print("Kaithakulam House")
        print("Vellarikund")
        print("Kasaragod")
        print("Kerala")
    address()


@student_details
def name_1():
    print("Student name is Nitha MAthew")
    print("Age is 36")
@student_details
def name_2():
    print("Student name is Nissy MAthew")
    print("Age is 42")
@student_details
def name_3():
    print("Student name is Sherin MAthew")
    print("Age is 38")
