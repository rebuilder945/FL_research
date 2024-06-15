def print_matrix(n):
    n = int(input())
    for i in range(1, n+1):
        for j in range(1, n+1):
            print((i+j-1) % n + 1, end=" ")
        print()

number=eval(input())
print_matrix(number)



