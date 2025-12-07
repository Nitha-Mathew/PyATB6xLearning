# A text file named "matter.txt" contains some text, which needs to be displayed such that
# every next character is separated by a symbol "#".
# Write a function definition for hash_display() in Python that would display
# the entire content of the file matter.txt in the desired format.

def hash_display():
    str1=''
    with open('matter.txt','r') as f:
        x=f.read()
        for i in x:
            str1=str1+i+'#'
    return str1
print(hash_display())