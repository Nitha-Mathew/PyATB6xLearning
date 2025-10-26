# Write a function half_and_half that takes in a list and change the list
# such that the elements of the second half are now in the first half.



def half_and_half(lst):
    lst1 = []
    lst2 = []
    if len(lst) % 2 == 0:
        l = len(lst) // 2
        for i in range(0, len(lst), 1):
            if i >= l:
                lst2 = lst2 + [lst[i]]
            else:
                lst1 = lst1 + [lst[i]]
        return lst2 + lst1
    else:
        l = (len(lst) - 1) // 2
        for i in range(0, len(lst), 1):
            if i > l:
                lst2 = lst2 + [lst[i]]
            elif i < l:
                lst1 = lst1 + [lst[i]]
            else:
                a = lst[i]
        return lst2 + [a] + lst1


half_and_half([10, 20, 30, 40, 50, 60, 70])

