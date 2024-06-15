def print_matrix(n):
        b=[1]*n
        for j in range(1,n+1):
            for i in range(j-1,n):
                b[i]=j
            for k in b:
                print(k,end=' ')
            print('')

number=eval(input())
print_matrix(number)



