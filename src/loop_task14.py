''' Write a python program to implement replace method using loop. If sub_str is found in my_str then it will replace the first
#### occurrence of sub_str with new_str else it will will print sub_str not found:-
Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',
sub_str = 'Peck', new_str = 'Pack' '''

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str = 'Pack'
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
if sub_str in lst:
    lst[lst.index(sub_str)] = new_str
else:
    print("substring not found")
for i in lst:
    for j in range(0,len(i),1):
        str2=str2+i[j]
    str2=str2+' '
print(str2)
