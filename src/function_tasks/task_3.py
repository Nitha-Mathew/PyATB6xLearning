# Define a function calls addFirstAndLast(x) that takes in a list of numbers and returns the sum of the first and last numbers.
# In - addFirstAndLast([])
# Out - 0
# In - addFirstAndLast([2, 7, 3])
# Out - 5
# In - addFirstAndLast([10])
# Out - 10

def addFirstAndLast(lst):
    s=0
    if len(lst)>1:
        s=lst[0]+lst[-1]
        return s
    elif bool(lst)==False:
        return 0
    else:
        return lst[0]

#addFirstAndLast([2,7,3])
#addFirstAndLast([])
addFirstAndLast([10])