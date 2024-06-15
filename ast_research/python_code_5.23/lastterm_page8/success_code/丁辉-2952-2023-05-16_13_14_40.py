def print_matrix(n):
    for r in range(n):
        for c in range(n):
            print(min(r,c)+1,end=' ')
        print()


number=eval(input())
print_matrix(number)



