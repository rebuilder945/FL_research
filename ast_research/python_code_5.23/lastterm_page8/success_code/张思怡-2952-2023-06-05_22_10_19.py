def print_matrix(n):
        for i in range(n):
            for j in range(n):
                print(min(i,j)+1,end=' ')
            print()

number=eval(input())
print_matrix(number)



