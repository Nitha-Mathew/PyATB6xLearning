#Write a Python program which takes two list as input and returns True if they have at least 3 common elements.
#inp_lst1 = [10,20,'Python', 10.20, 10+20j, [10,20,30], (10,20,30)]
#inp_lst2 = [(10,20,30),1,20+3j,100.2, 10+20j, [10,20,30],'Python']
#Output:- True
lst=[10,20,'Python', 10.20, 10+20j, [10,20,30], (10,20,30)]
lst1=[(10,20,30),1,20+3j,100.2, 10+20j, [10,20,30],'Python']
c=0
for i in lst:
    if i in lst1:
        c=c+1
if c>=3:
    print('True')
else:
    print('false')
