def print_matrix(n):
    matric=[[0 for c in range(n)]for r in range(n)]
    for r in range(n):
        for c in range(n):
            for i in range(n):
                if min(r,c)==i+1:
                    matric[r][c]=i+1
    for r in range(n):
        for c in range(n):
            print(matric[r][c],end=" ")
        print()

number=eval(input())
print_matrix(number)



