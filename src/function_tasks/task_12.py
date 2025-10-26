# Write a function that accepts a dictionary as an argument. If the dictionary contains replicate values,
# return an empty dictionary, otherwise, return a new dictionary whose values are now the keys and whose
# keys are the values.

def fun_dict(dict):
    lst=[]
    dict1={}
    for i,j in dict.items():
        lst=lst+[j]
    for i in lst:
        if lst.count(i)>1:
            return {}
        else:
            for i,j in dict.items():
                dict1[j]=i
            return dict1
def main():
    x=fun_dict({1:'Nitha', 2:'Mathew', 3:'Laya',4:'Nitha',5:'Laya'})
    y=fun_dict({1:'Nitha', 2:'Mathew', 3:'Laya',4:'Anna',5:'Nissy'})
    return x,y

main()