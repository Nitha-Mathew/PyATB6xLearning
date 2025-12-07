# Write a function in Python to count the words "this" and "these" present in a text file "article.txt".
# [Note that the words "this" and "these" are complete words]
def count_words():
    s=0
    e=0
    with open('article.txt','r') as f:
        x=f.read()
        lst=x.split()
        for i in lst:
            if i=='this':
                s+=1
            elif i=='these':
                e+=1
    return s,e
this,these=count_words()
print('Number of This is', this)
print('Number of these is', these)
