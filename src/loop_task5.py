'''Q. Write a Python program to find the total number of times letter 'p' is appeared in the below string using loop:-
Input:- 'peter piper picked a peck of pickled peppers.\n'''''

my_str='peter piper picked a peck of pickled peppers.\n'
c=0
for i in my_str:
    if i=='p':
        c+=1
print(c)