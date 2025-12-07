# Write a function in python to read the content from
# a text file "poem.txt" line by line and display the same on screen.

def poem():
    with open('poem.txt', 'r') as f:
        f.seek(157)
        x = f.readline()
        # for x in f:
        print(x)


poem()