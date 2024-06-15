def print_matrix(n):
    matric = [[0 for c in range(n)]for r in range(n)]
    for r in range(n):
        for c in range(n):
            if r + c < n-1:
                matric[r][c] = 1
            elif r+c ==n-1:
                matric[r][c] = 2
            else:
                matric[r][c] = 3
    for i in range(n):
        for c in range(n):
            print(matric[r][c],end=" ")
        print()

number=eval(input())
print_matrix(number)



