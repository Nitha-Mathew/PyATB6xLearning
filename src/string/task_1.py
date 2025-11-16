sentence=input("Enter the sentence: ")
v=0
c=0
sentence=sentence.lower()
sentence=sentence.strip()
sentence=sentence.replace(" ","")
for i in sentence:
    print(i)
    if i in ['a','e','i','o','u']:
        v=v+1
    else:
        c=c+1
print("vowels = ",v)
print("consonant = ",c)