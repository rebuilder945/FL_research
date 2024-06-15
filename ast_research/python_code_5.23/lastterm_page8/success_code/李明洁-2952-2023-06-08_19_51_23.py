def print_matrix(n):
        xi = [[0 for c in range(0,n)] for r in range(n)]
        for r in range(n):
            for c in range(n):
                print(min(r,c)+1,end = " ")
            print()

number=eval(input())
print_matrix(number)



