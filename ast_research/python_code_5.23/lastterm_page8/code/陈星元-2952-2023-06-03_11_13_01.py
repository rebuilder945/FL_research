def print_matrix(n):
    ls=[[0 for c in range(n)]for r in range(n)]
        for r in range(n):
            for c in range(n):
                ls[r][c]=min(r,c)+1
        for r in range(n):
            for c in range(n-1):
                print(ls[r][c],end=" ")
            print(ls[r][n-1])
        

number=eval(input())
print_matrix(number)



