# A binary file "STUDENT.DAT" has structure (admission_number, Name, Percentage).
# Write a function count_rec() in Python that would read contents of the file "STUDENT.DAT"
# and display the details of those students whose percentage is above 75.
# Also display number of students scoring above 75%

import pickle
def enter_rec():
    with open('Student.dat','ab') as f:
        Adm=int(input('Enter the Admission No.: '))
        Name=input('Enter the Name: ')
        Percent=int(input('Enter the percentage: '))
        t=[Adm,Name,Percent]
        pickle.dump(t,f)
def count_rec():
    c=0
    with open('Student.dat','rb') as f:
        try:
            while True:
                x=pickle.load(f)
                if x[2]>75:
                    print("Student name is {} and Admission number is {}".format(x[1],x[0]))
                    c+=1
        except:
            return c
#enter_rec()
count_rec()
