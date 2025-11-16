rows=5
for i in range (0,rows+1):
    for j in range(i):
        print(' ', end=' ')
    for k in range(rows-2*i):
        print('*',end=' ')
    print()
