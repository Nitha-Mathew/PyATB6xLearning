# Write a function in Python to count uppercase character in a text file.
def uppercase():
    c=0
    with open('story.txt','r') as f:
        x=f.read()
        for i in x:
            if i.isupper():
                c+=1
    return c
print(uppercase())