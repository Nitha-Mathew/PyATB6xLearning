'''Q. W. A P. to implement calculator but the operation to be done and two numbers will be taken as input from user:-
Operation console should show below:-
Please select any one operation from below:-
To add enter 1
to subtract enter 2
To multiply enter 3
To divide enter 4
To divide and find quotient enter 5
To divide and find remainder enter 6
To divide and find num1 to the power of num2 enter 7
To Come out of the program enter 8'''

def operation():
    Op= int(input('''Please select any one operation from below:-
    To add enter 1
    to subtract enter 2
    To multiply enter 3
    To divide enter 4
    To divide and find quotient enter 5
    To divide and find remainder enter 6
    To divide and find num1 to the power of num2 enter 7
    To Come out of the program enter 8: '''))
    if Op==1:
        x= int(input("Enter the first number: "))
        y= int(input("Enter the second number: "))
        print(x)
        print(y)
        z=x+y
        print(f'Sum is: ',z)
        operation()
        print()
    elif Op==2:
        x= int(input("Enter the first number: "))
        y= int(input("Enter the second number: "))
        z=x-y
        print(f'Difference is:',z)
        operation()
        print()
    elif Op==3:
        x= int(input("Enter the first number: "))
        y= int(input("Enter the second number: "))
        z=x*y
        print(f'Product is:',z)
        operation()
        print()
    elif Op==4:
        x= int(input("Enter the first number: "))
        y= int(input("Enter the second number: "))
        z=x/y
        print(f'Division is:',z)
        operation()
    elif Op==5:
        x= int(input("Enter the first number: "))
        y= int(input("Enter the second number: "))
        z=x//y
        print(f'Quoient is:',z)
        operation()
    elif Op==6:
        x= int(input("Enter the first number: "))
        y= int(input("Enter the second number: "))
        z=x%y
        print(f'Remainder is:',z)
        operation()
    elif Op==7:
        x= int(input("Enter the first number: "))
        y= int(input("Enter the second number: "))
        z=x/(y**2)
        print(f'Result is:',z)
        operation()
    elif Op==8:
        print("Exited")


operation()

