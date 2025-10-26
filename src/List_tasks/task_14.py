#Write a Python program to create a 3X4X6 3D matrix wiith below elements using loop
#Output:-
# [
#     [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
#     [[0,0,0,0,0,0],[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3]],
#     [[0,0,0,0,0,0],[2,2,2,2,2,2],[4,4,4,4,4,4],[6,6,6,6,6,6]]
# ]
ls=[0,0,0]
lst=[0,0,0,0]
lst1=[]
lst2=[0,0,0,0]
lst3=[0,0,0,0]
for k in range(0,3):
    if k==0:
        for j in range(0,4):
            for i in range(0,6):
                lst1=lst1+[0]
            lst[j]=lst1
            lst1=[]
        ls[k]=lst
    elif k==1:
        for j in range(0,4):
            for i in range(0,6):
                lst1=lst1+[j]
            lst2[j]=lst1
            lst1=[]
        ls[k]=lst2
    elif k==2:
        l=0
        for j in range(0,4):
            for i in range(0,6):
                lst1=lst1+[l]
            l=l+2
            lst3[j]=lst1
            lst1=[]
        ls[k]=lst3
print(ls)