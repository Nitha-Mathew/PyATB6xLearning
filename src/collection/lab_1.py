from collections import *

#counter
#data=input("Enter the data")
#count_char=Counter(data)
#print(count_char)

#named tuple
data=namedtuple(typename="data", field_names=["name", "age", "place", "residing"])
t=data("Nitha", "36", "Vellarikund", "Qatar")
g=data("Sherin","38","Vellarikund","Bangalore")
print(g.name)
print(t.age)
print(t.place)
print(t.residing)