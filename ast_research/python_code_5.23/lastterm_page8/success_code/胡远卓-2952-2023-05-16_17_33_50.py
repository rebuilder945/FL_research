def print_matrix(n):
    for i in range(1,n+1):
        for j in range(1,n):
            print(min(i,j),end=' ')
        print(min(i,n))

number=eval(input())
print_matrix(number)



