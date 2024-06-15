def print_matrix(n):
        for x in range(1,n+1):
            for y in range(1,n+1):
                a=min(x,y)
                print(a,end=' ')
            print()

number=eval(input())
print_matrix(number)



