r=int(input("Enter the required row: "))
c=int(input("Enter the required column: "))
if r==c:
    for i in range(r):
        for j in range(c):
            if j<=i:
                print("*", end=' ')
                j=0
        print(sep='/n')
else:
    print("Not possible")