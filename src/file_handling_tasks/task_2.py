# Write a function in python to count the number of lines
# from a text file "story.txt" which is not starting with an alphabet "T".


def story():
    c = 0
    with open('story.txt', 'r') as f:
        x = f.readlines()
        for i in x:
            if i[0] != 'T':
                c += 1
    print(c) 


story()
