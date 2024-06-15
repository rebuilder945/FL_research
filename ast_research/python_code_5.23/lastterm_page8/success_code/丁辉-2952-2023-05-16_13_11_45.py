def print_matrix(n):
    a=[[0 for c in range(n)] for r in range(n)]
    for r in range(n):
        for c in range(n):
            a[r][c]=min(r,c)+1
    print(a[r][c],end=' ')

number=eval(input())
print_matrix(number)



