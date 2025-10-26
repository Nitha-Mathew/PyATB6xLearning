#Write a Python program to copy a list using loop.
#inp_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]
#out_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]
lst=[10,10.20,10+20j, 'Python', [10,20], (10,20)]
lst1=[]
for i in lst:
    lst1=lst1+[i]
print(lst1)
