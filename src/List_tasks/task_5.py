#Write a Python program to sort a list in ascending order using loop.
#Input:- [100,10,1,298,65,483,49876,2,80,9,9213]
#Output:- [1,2,9,10,65,80,100,298,483,9213,49876]

lst=[100,10,1,298,65,483,49876,2,80,9,9213]
l=len(lst)
lst2=[]
for i in range(0,l,1):
    j=min(lst)
    lst2=lst2+[j]
    lst.remove(j)
print(lst2)
