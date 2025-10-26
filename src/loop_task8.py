'''Write a python program to find below output using loop:-
Input:- 'peter piper picked a peck of pickled peppers.'
Output:- 'peppers pickled of peck a picked piper peter'  '''

my_str='peter piper picked a peck of pickled peppers.'
lst=[]
str1=''
str2=''
for i in my_str:
    if i!=' ':
        str1=str1+i
    else:
        lst=lst+[str1]
        str1=''
lst=lst+[str1]
for i in range(-1,-len(lst)-1,-1):
    str2=str2+lst[i]+' '
print(str2)
