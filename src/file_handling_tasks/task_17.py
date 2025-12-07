# A binary file players.dat, containing records of following list format: [code, name, country and total runs]

# 1. Write a python function that display all records where player name starts from 'A'
# 2. Write a python function that accept country as an argument and count and display
#     the number of players of that country.
# 3. Write a python function that add one record at the end of file.

def enter_rec():
    with open('players.dat', 'ab+') as f:
        code = int(input("Enter the code: "))
        name = (input("Enter the Name: "))
        country = (input("Enter the country: "))
        total_runs = int(input("Enter the total runs: "))
        lst = [code, name, country, total_runs]
        pickle.dump(lst, f)


def display():
    f = open('players.dat', 'rb')
    try:
        while True:
            x = pickle.load(f)
            if x[1].startswith('A'):
                print("Name is {},Code is {}, Country is {}, Total runs is {}".format(x[1], x[0], x[2], x[3]))
    except:
        f.close()


def count_display(country):
    c = 0
    f = open('players.dat', 'rb')
    try:
        while True:
            x = pickle.load(f)
            for i in x:
                if i == country:
                    c += 1
    except:
        f.close()
        return c


def add_rec():
    with open('players.dat', 'ab+') as f:
        code = int(input("Enter the code: "))
        name = (input("Enter the Name: "))
        country = (input("Enter the country: "))
        total_runs = int(input("Enter the total runs: "))
        lst = [code, name, country, total_runs]
        pickle.dump(lst, f)


# enter_rec()
# display()
count_display(input("Enter the country: "))
add_rec()
