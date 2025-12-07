# A binary file "Book.dat" has structure [BookNo, Book_Name, Author, Price].
# i. Write a user defined function createFile() to input data for a record and add to Book.dat.
# ii. Write a function countRec(Author) in Python which accepts the Author name as parameter
# and count and return number of books by the given Author are stored in the binary file "Book.dat"
import pickle
def createFile():
    with open('Book.dat','ab') as f:
        Num=int(input('Enter the Book No.: '))
        Name=input('Enter the Book Name: ')
        Author=input('Enter the Author: ')
        Price=int(input('Enter the price: '))
        records=[Num,Name,Author,Price]
        pickle.dump(records,f)


def countRec(Author):
    c=0
    with open('Book.dat','rb') as f:
        try:
            while True:
                x=pickle.load(f)
                if Author==x[2]:
                    c=c+1
        except:
            return c
#createFile()
countRec(input('Enter the Author: '))