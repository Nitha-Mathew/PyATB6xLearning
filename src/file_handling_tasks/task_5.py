# Write a function display_words() in python to read lines from a text file "story.txt",
# and display those words, which are less than 4 characters.

def display_words():
    c=0
    with open('story.txt','r') as f:
        x=f.read()
        lst=x.split()
        for i in lst:
            if len(i)<4:
                c+=1
    return c
print(display_words())