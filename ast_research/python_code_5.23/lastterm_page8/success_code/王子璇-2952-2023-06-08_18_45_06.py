def print_matrix(n):
        for a in range(n):
            for b in range(a):
                print(b+1,end=' ')
            for c in range(a,n):
                print(a+1,end=' ')
            print()

number=eval(input())
print_matrix(number)



