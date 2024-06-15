def print_matrix(n):
    global m
    b=[1]*n
    ls=[]
    for i in range(n):
        ls.append(b[:])
    if n>=2:
        for i in range(1,n):
            ls[i][i]=i+1
            m=1
            for j in range(1,i):
                ls[i][j]=m+1
                m=m+1
            for k in range(i+1,n):
                ls[i][k]=i+1
    for i in ls:
        print(' '.join(str(x) for x in i))

number=eval(input())
print_matrix(number)



