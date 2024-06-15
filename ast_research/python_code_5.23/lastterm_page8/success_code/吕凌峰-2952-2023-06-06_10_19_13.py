def print_matrix(n):
     for i1 in range(1, n + 1):
            for i2 in range(1, n + 1):
                if i2 <= i1:
                    print("%i "%i2, end='')
                else:
                    print("%i "%i1, end='')
            print()

number=eval(input())
print_matrix(number)



