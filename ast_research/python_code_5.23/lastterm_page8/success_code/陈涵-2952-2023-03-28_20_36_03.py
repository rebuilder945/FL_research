def print_matrix(n):
    for i in range(1,n+1):
        num=[str(min([i,j])) for j in range(1,n+1) ]
        print(" ".join(num))

number=eval(input())
print_matrix(number)



