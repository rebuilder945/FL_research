def print_matrix(n):
        c=0
        for x in range(1,n+1):
            c=x
            q=0
            for y in range(1,n+1):
                if y<x:
                    print("%d "%y,end="")
                    y+=1
                    q+=1
                else:
                    print("%d "%x,end="")
                    q+=1
                if q==n:
                    print()

number=eval(input())
print_matrix(number)



