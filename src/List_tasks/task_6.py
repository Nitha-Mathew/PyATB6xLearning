#Write a Python program to get a sorted list in increasing order of last element in each tuple in a given list using loop.
#Input:- [(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]
#output:- [(9,1),(2,3),(5,4),(5,5),(7,6),(5,9)]

lst=[(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]
lst1=[]
lst2=[]
lst3=[]
for i in lst:
    lst1=lst1+[i[1]]
l=len(lst1)
for i in range(0,l,1):
    j=min(lst1)
    lst2=lst2+[j]
    lst1.remove(j)
for i in lst2:
    for j in lst:
        if i ==j[1]:
            lst3=lst3+[j]
print(lst3)
