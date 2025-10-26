#Write a Python program to find the smallest number from a list using loop.
#Input:- [10,100,2321, 1,200,2]
#Output:- 1
lst=[10,100,2321, 1,200,2]
s=lst[0]
for i in range(1,len(lst),1):
    if s>lst[i]:
        s=lst[i]
print(s)
