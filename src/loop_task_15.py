''' Write a python program to find below output (implements rjust and ljust) using loop:-
Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str =
'Peck',
Output:- '*********************Peck********************' '''

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
str1=''
for i in range(0,my_str.index(sub_str),1):
    str1=str1+'*'
for i in range(0,len(sub_str),1):
    str1=str1+sub_str[i]
for i in range(0,len(my_str)-my_str.index(sub_str)-len(sub_str),1):
    str1=str1+'*'
print(str1)