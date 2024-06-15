def print_matrix(n):
        a = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                a[i][j]=min(i,j)
        print(a) 

number=eval(input())
print_matrix(number)



