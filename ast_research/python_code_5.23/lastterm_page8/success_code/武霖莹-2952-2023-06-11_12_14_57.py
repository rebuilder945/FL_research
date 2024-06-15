def print_matrix(n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end=' ')
            for x in range(n-i):
                print(i,end=' ')
            print()

number=eval(input())
print_matrix(number)



