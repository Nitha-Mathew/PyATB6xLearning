# Given a binary file game.dat, containing records of following list format: [game_name, participants]

# Write a function in Python that would read contents from the file game.dat and
# creates a file named basket.dat copying only those records from game.dat where the game name is "Basket Ball"

def add_contents():
    with open('game.dat', 'ab+') as f:
        game_name = (input("Enter the game: "))
        participants = int(input("Enter the number of participants: "))
        lst = [game_name, participants]
        pickle.dump(lst, f)


def read_contents():
    f = open('game.dat', 'rb')
    try:
        while True:
            x = pickle.load(f)
            if x[0] == 'basket ball':
                with open('basket.dat', 'ab') as file:
                    lst1 = []
                    for i in x:
                        lst1 = lst1 + [i]
                    pickle.dump(lst1, file)
                with open('basket.dat', 'rb') as file:
                    x = pickle.load(file)
                    print(x)
    except:
        f.close()


read_contents()