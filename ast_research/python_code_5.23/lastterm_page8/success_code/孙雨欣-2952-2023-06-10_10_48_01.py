def print_matrix(n):
    ls1=[[1+x for x in range(n)]for y in range(n)]
    for i in range(0,n):
        for j in range(i+1,n):
            ls1[i][j]=str(1+i)
        print(' '.join(str(ls1[i])))

number=eval(input())
print_matrix(number)



