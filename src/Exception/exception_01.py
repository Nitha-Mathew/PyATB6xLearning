a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
try:
    c=a/b
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("program completed")




