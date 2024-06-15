def print_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            matrix[i][j] = i + 1
    
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")

number=eval(input())
print_matrix(number)



