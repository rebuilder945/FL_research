def print_matrix(n):
        a = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            print('')
            for j in range(n):
                a[i][j]=str(min(i+1,j+1))
                print(a[i][j]+" ",end="")

number=eval(input())
print_matrix(number)



