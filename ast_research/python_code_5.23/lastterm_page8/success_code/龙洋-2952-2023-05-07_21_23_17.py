def print_matrix(n):
        lis=[0 for x in range(n)]
        for x in range(n):
            for y in range(n-x):
                lis[x+y]=lis[x+y]+1
            lis1=[str(x) for x in lis]
            print(' '.join(lis1))

number=eval(input())
print_matrix(number)



