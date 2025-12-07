# Given a binary file employee.dat, created using dictionary object having keys: (empcode, name, and salary)

# Write a python function that add one more record at the end of file.
# Write a python function that display all employee records whose salary is more that 30000
import pickle


def rec_creation():
    with open('employee.dat', 'ab') as f:
        empcode = int(input("Enter the Emp ID: "))
        name = (input("Enter the Name: "))
        salary = int(input("Enter the Salary: "))
        d = {'empcode': empcode, 'name': name, 'salary': salary}
        pickle.dump(d, f)


def add_emp():
    with open('employee.dat', 'ab') as f:
        empcode = int(input("Enter the Emp ID: "))
        name = (input("Enter the Name: "))
        salary = int(input("Enter the Salary: "))
        d = {'empcode': empcode, 'name': name, 'salary': salary}
        pickle.dump(d, f)


def emp_rec():
    f = open('employee.dat', 'rb')
    try:
        while True:
            x = pickle.load(f)
            if x['salary'] > 30000:
                print("Employee name is {} and Employee ID is {}".format(x['name'], x['empcode']))
    except:
        f.close()


# rec_creation()
# add_emp()
emp_rec()
