# Write a function in Python to count and display the total number of words in a text file.
def count_and_display():
    with open('poem.txt','r') as f:
        x=f.read()
        lst=x.split()
        print(len(lst))
count_and_display()