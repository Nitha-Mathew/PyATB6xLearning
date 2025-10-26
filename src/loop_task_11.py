'''Write a python program to find below output using loop:-
Input:- 'peter piper picked a peck of pickled peppers.'
Output:- 'Peter Piper Picked A Peck Of Pickled Peppers' '''

my_str= 'peter piper picked a peck of pickled peppers.'
str1=''
lst =[]
str2=''
for i in my_str:
    if i!=' ':
        str1=str1+i
    else:
        lst=lst+[str1]
        str1=''
lst=lst+[str1]
for i in lst:
    for j in range(0,len(i),1):
        if j==0:
            str2=str2+i[j].upper()
        else:
            str2=str2+i[j]
    str2=str2+' '
print(str2)