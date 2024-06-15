def print_matrix(n):
        for i in range(1, n+1):
            row = []
            for j in range(1, n+1):
                num = min(i, j, n-i+1, n-j+1)
                row.append(str(num))
            print(" ".join(row))


number=eval(input())
print_matrix(number)



