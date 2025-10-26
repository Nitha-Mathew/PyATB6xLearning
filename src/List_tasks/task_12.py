#Write a Python program to create a 4X4 2D matrix with below elements using loop and list comprehension both.
#Output:- [[0,0,0,0],[0,1,2,3],[0,2,4,6],[0,3,6,9]]
lst1=[]
lst2=[]
lst3=[]
lst4=[]
for k in range(0,4):
    if k==0:
        for i in range(0,4):
            lst1=lst1+[0]
        lst[k]=lst1
    elif k==1:
        for i in range(0,4,1):
            lst2=lst2+[i]
        lst[k]=lst2
    elif k==2:
        for i in range(0,7,2):
            lst3=lst3+[i]
        lst[k]=lst3
    elif k==3:
        for i in range(0,10,3):
            lst4=lst4+[i]
        lst[k]=lst4
print(lst)
