# A binary file school.dat has structure(rollno, name, class, fees)

# Write a definition for function total_fees( ) that reads each object of file and calculate
# the total fees of students and display the same.

import pickle

def enter_rec():
    with open('school.dat','ab+') as f:
        rollno=int(input("Enter the Roll no.: "))
        name=(input("Enter the Name: "))
        class_no=int(input("Enter the Class: "))
        fees=int(input("Enter the fees: "))
        lst=[rollno,name,class_no,fees]
        pickle.dump(lst,f)
def total_fees():
    fees_total=0
    f=open('student1.dat','rb')
    try:
        while True:
            x=pickle.load(f)
            print(x)
            fees_total=fees_total+x[3]
    except:
        f.close()
        return fees_total
#enter_rec()
total_fees()