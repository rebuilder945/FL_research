def print_matrix(n):
    for i in range(n):
        for j in range(n):
            a=min([i,j])+1
            print(a,end=" ")
        print()

number=eval(input())
print_matrix(number)



