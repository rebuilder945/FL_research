def print_matrix(n):
    for i in range(n):
        num=[str(min([i,j])) for j in range(n) ]
        print(" ".join(num))

number=eval(input())
print_matrix(number)



