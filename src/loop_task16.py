''' Write a python program to find below output using loop:-
Input:- 'This is Python class', sep = ' is',
Output:- ['This', 'is', 'Python class'] '''

my_str ='This is Python class'
sep='is'
lst = []
str1=''
str2=''
for i in my_str:
    if i!=' ':
        str1=str1+i
    else:
        if str2!=sep:
            lst=lst+[str1]
            str2=str1
            str1=''
        else:
            str2=str1
            str1=str1+' '
lst=lst+[str1]
print(lst)