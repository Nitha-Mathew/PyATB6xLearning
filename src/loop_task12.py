'''Write a python program to find below output using loop:-
Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
Output:- 'Peter piper picked a peck of pickled peppers' '''

my_str= 'peter piper picked a peck of pickled peppers.'
str2=''
for i in range(0,len(my_str)-1,1):
    if i==0:
        str2=str2+my_str[i].upper()
    else:
        str2=str2+my_str[i]
print(str2)