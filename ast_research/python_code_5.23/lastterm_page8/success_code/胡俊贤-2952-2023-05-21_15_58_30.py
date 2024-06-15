def print_matrix(n):
    for i in range(1,n+1):
        x=1
        for a in range(1,n+1):
            if x<i:
                print(x,end=' ')
                x+=1
            elif x==i:
                print(x)
        print()

number=eval(input())
print_matrix(number)



