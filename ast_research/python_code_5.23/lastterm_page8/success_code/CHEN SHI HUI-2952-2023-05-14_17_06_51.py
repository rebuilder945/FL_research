def print_matrix(n):
    a=[1]
    b=a*n  
    for i in range(1,n+1):
        for j in range(i,n+1):
            b[j-1]=i
        for k in b:
            print(k,end=' ')
        print('\n')


number=eval(input())
print_matrix(number)


