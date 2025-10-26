#Write a Python program which takes a list of numbers as input and prints a new list after removing even numbers from it.
#Input:- [10,21,22,98,87,45,33,1,2,100]
#Output:- [21,87,45,33,1]
lst=[10,21,22,98,87,45,33,1,2,100]
lst1=[lst[i] for i in range(0,len(lst),1) if lst[i]%2!=0]
print(lst1)