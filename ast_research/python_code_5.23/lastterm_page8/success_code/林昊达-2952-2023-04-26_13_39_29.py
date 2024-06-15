def print_matrix(n):
        for i in range(1,n+1):
            for t in range(1,i):
                print(t,end=" ")
            for j in range(i,n+1):
                print(i,end=" ")
            print()

number=eval(input())
print_matrix(number)



