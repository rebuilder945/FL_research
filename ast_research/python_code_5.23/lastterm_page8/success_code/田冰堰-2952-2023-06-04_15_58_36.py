def print_matrix(n):
    matric=[[0 for c in range(n)]for r in range(n)]
    for r in range(n):
        for c in range(n):
            for i in range(1,n+1):
                if min(r,c)==i:
                    matric[r][c]=i
    for r in range(n):
        for c in range(n):
            print(matric[r][c],end=" ")
        print()

number=eval(input())
print_matrix(number)



