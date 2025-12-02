#raise exception deliberately
#the response of the raise is given in except block
num=int(input("Enter the number: "))
if num>10:
    raise Exception("Number out of range")
print(num)






