# Write a function AMCount() in Python, which should read each character of a text file STORY.TXT,
# should count and display the occurance of alphabets A and M (including small cases a and m too).
# For Example:
# If the file content is as follows:
# Updated information
# As simplified by official websites.
# The EUCount() function should display the output as:
# A or a:4
# M or m :2

def AMCount():
    a=0
    m=0
    with open('STORY1.TXT','r') as f:
        x=f.read()
        for i in x:
            if i=='A' or i=='a':
                a+=1
            elif i=='M' or i=='m':
                m+=1
    return a,m
a,m=AMCount()
print('A or a:',a)
print('M or m:',m)