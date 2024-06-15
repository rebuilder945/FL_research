def print_matrix(n):
        a=[[0 for x in range(n)]for y in range(n)]
        for i in range(1,n+1):
            for m in range(n):
                a[i-1][m]=i
                a[m][i-1]=i
        for t in a:
            print(" ".join([str(y) for y in t]))

number=eval(input())
print_matrix(number)



