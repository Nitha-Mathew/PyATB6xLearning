'''Write a python program to find below output using loop:-
Input:- 'peter piper picked a peck of pickled peppers.'
Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled','peppers']'''

my_str='peter piper picked a peck of pickled peppers.'
lst=[]
str1=''
for i in my_str:
    if i!=' ':
        str1=str1+i
    else:
        lst=lst+[str1]
        str1=''
lst=lst+[str1]
print(lst)