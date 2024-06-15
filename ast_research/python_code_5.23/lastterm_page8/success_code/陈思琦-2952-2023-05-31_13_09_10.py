def print_matrix(n):
        b=0
        for x in range(1,n+1):
            for y in range(1,n+1):
                a=min(x,y)
                print(a,end=' ')
                b+=1
            if b==n:
                b=0
                print('')
                    

number=eval(input())
print_matrix(number)



