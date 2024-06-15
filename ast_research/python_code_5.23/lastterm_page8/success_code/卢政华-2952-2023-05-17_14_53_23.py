def print_matrix(n):
        for i in range(1, n+1):
            row = []
            for j in range(1, n+1):
                num = min(i, j)
                row.append(str(num))
            print(" ".join(row))

number=eval(input())
print_matrix(number)



