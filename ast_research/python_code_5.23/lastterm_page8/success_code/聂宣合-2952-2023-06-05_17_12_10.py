def print_matrix(n):
    for i in range(n):
        for j in range(n):
            print(min(i,j),end=" ")

number=eval(input())
print_matrix(number)



