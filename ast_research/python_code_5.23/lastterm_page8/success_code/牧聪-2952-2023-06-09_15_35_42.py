def print_matrix(n):
    for x in range(1,n+1):
        a=" ".join(str(t) for t in range(1,x+1))
        b=(str(x)+" ")*(n-x)
        print(a+" "+b)
        

number=eval(input())
print_matrix(number)



