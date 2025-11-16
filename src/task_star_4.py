rows=5

for i in range(1,rows):
    for j in range(rows-i):
        print(' ', end=' ')
    for k in range(i):
        print('*',end=' ')
        if i>2:
            for l in range(2*i-1):
                print(' ',end=' ')

    print()
