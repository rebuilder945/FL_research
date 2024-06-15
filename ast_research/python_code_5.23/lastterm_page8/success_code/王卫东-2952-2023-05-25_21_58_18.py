def print_matrix(n):
    a=[1]
    b=a*n
    for x in range(1,n+1):
        for y in range(x,n+1):
            b[y-1]=x
        for m in b:
            print(m,end=' ')
        print('\n')

number=eval(input())
print_matrix(number)



