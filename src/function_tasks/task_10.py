# Write a method in python to display the elements of list thrice if it is a number and display
# the element terminated with ‘#’ if it is not a number.


def termination(lst):
    for i in lst:
        if i.isnumeric():
            i=i*3
            print(i)
        elif i.isalpha():
            i=i+'#'
            print(i)
ThisList=['41','DROND','GIRIRAJ', '13','ZARA']
termination(ThisList)