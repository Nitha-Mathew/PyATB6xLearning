# Write a function to search and display details of student whose rollno is '1005'
# from the binary file student.dat having structure [rollno, name, class and fees].

import pickle


def enter_rec():
    with open('student1.dat', 'ab+') as f:
        rollno = int(input("Enter the Roll no.: "))
        name = (input("Enter the Name: "))
        class_no = int(input("Enter the Class: "))
        fees = int(input("Enter the fees: "))
        lst = [rollno, name, class_no, fees]
        pickle.dump(lst, f)


def search_display():
    f = open('student1.dat', 'rb')
    try:
        while True:
            x = pickle.load(f)
            if x[0] == 1005:
                print("Student name is {} ,Class is {} and fees paid is {}".format(x[1], x[2], x[3]))
    except:
        f.close()


# enter_rec()
search_display()