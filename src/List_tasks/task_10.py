#Write a Python program to find the list of words that are longer than or equal to 4 from a given string.
#Input:- 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
#Output:- ['much', 'wood', 'would', 'woodchuck', 'chuck', 'could']
#Note:- Duplicate should be avoided.
str1='How much wood would a woodchuck chuck if a woodchuck could chuck wood'
lst1=str1.split()
lst=[]
lst2=[]
for i in lst1:
    if len(i)>=4:
        lst=lst+[i]
for i in lst:
    if i not in lst2:
        lst2=lst2+[i]
print(lst2)

