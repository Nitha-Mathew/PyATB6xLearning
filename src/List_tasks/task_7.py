#Write a Python program to remove fuplicate element from a list using loop.
#Input:- [10,1,11,1,29,876,768,10,11,1,92,29,876]
#Output:- [10,1,11,29,876,768,92]
lst=[10,1,11,1,29,876,768,10,11,1,92,29,876]
lst1=[]
for i in lst:
    if lst.count(i)==1:
        lst1=lst1+[i]
for i in lst:
    if lst.count(i)>1:
        lst1=lst1+[i]
        lst.remove(i)
print(lst1)

