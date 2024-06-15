def print_matrix(n):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                num = min(i, j, n - i + 1, n - j + 1)
                print(num, end=" ")
            print()

number=eval(input())
print_matrix(number)



