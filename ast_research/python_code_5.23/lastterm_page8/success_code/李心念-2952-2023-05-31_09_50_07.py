def print_matrix(n):
    a = [[min(x,y) for x in range(1,n+1)] for y in range(1,n+1)]
    for i in a:
        for h in i:
            print(h,end=' ')
            if h==n-1:
                print('\n')

number=eval(input())
print_matrix(number)



