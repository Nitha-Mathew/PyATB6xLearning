'''  Write a python program to implement index method using loop. If sub_str is found in my_str then it will print the index
#### of first occurrence of first character of matching string in my_str:-
Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',
sub_str = 'Pickl' '''

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Pickl'
l = len(sub_str)
k = 0
for i in range(0, len(my_str) - 4, 1):
    if my_str[k:l:1] == sub_str:
        print(k)
    k = k + 1
    l = l + 1
