def print_matrix(n):
    
        s=""
        for i in range(1,n+1):
            s=s+str(i)
        a=1
        for x in range(1,n+1):
            b=s[:a]+str(x)*(n-1)
            print(' '.join(b))
            a=a+1
            n-=1
            
           

number=eval(input())
print_matrix(number)



