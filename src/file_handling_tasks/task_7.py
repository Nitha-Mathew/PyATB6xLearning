# Write a function in Python to count words in a text file those are ending with alphabet "e"

def ending_with_e():
    c=0
    with open('story.txt','r') as f:
        x=f.read()
        lst=x.split()
        for i in lst:
            if i[-1]=='e':
                c+=1
    return c
print(ending_with_e())