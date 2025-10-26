'''Write a Python Program, to print all the indexes of all occurences of
letter 'p' appeared in the string using loop:-
Input:- 'peter piper picked a peck of pickled peppers.'''

my_str='peter piper picked a peck of pickled peppers.'
for i in range(0,len(my_str)-1):
    if my_str[i] =='p':
        print (i)