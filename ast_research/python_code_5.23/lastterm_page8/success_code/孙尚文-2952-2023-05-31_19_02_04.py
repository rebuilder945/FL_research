def print_matrix(n):
        x=[[0 for c in  range (n)]for r in range(n)]
        for r in range(n):
            for c in range(n):
                x[r][c]=min(r,c)+1
        for i in range(n):
            for j in range(n):
                print(x[i][j],end=" ")
            print()

number=eval(input())
print_matrix(number)



