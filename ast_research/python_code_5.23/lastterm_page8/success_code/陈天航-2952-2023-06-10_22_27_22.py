def print_matrix(n):
            for i in range(1, n+1):
                row = ""
                for j in range(1, n+1):
                    if i < j:
                        row += str(i) + " "
                    else:
                        row +=  str(j) + " "
                print(row)

number=eval(input())
print_matrix(number)



