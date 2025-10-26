#Write a Python program which takes a list from the user and prints it after reshuffling the elements of the list.
#Input:- [10,21,22,98,87,45,33,1,2,100]
#Output:- [1,87,21,10,33,2,100,45,98,22] (It may be any randon list but with same elements)
lst=[10,21,22,98,87,45,33,1,2,100]
lst1=list(set(lst))
print(lst1)

