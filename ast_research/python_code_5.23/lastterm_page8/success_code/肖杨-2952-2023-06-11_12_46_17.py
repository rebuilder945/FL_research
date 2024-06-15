def print_matrix(n):
            a=[]
            for i in range(n):
                a.append([0]*n)
            for x in range(n):
                for i in range(x,n):
                    for j in range(x,n):
                        a[i][j]=a[i][j]+1
            for i in a:
                print('\t',' '.join(map(str,i)))


number=eval(input())
print_matrix(number)



