def print_matrix(n):
    n = [[min(x,y) for x in range(1,n+1)] for y in range(1,n+1)]
    for i in n:
        for h in i:
            print(h,end=' ')

number=eval(input())
print_matrix(number)



