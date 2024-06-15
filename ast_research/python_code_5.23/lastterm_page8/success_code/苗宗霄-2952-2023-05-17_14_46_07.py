def print_matrix(n):
        for i in range(1, n+1):
            for j in range(i, i+n):
                num = ((j-1) % n) + 1
                print(num, end=' ')
            print()

number=eval(input())
print_matrix(number)



