def print_matrix(n):
    a=[[1 for x in range(n)]for y in range(n)]
    for x in range(n):
        for y in range(n):
            a[x][y]=min(x+1,y+1)
    for x in range(n):
        for y in range(n):
            print(a[x][y],end=' ')
        print()

number=eval(input())
print_matrix(number)



