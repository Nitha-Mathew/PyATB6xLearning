#Write a Python program to find the largest number from a list using loop.
#Input:- [10,100,2321, 1,200,2]
#Output:- 2321
lst=[10,100,2321, 1,200,2]
m=lst[0]
for i in range(1,len(lst),1):
    if m<lst[i]:
        m=lst[i]
print(m)

