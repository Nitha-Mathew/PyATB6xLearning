'''Write a python program to find below output using loop:-
Input:- 'peter piper picked a peck of pickled peppers.'
Output:- '.sreppep delkcip fo kcep a dekcip repip retep'  '''

my_str= 'peter piper picked a peck of pickled peppers.'
str1=''
for i in range(-1,-len(my_str)-1,-1):
    str1=str1+my_str[i]
print(str1)