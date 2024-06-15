def Fibonacci(x,y):
    x[0]=0
    for i in x:
        b=x.index(i)
        if b==0:
            x.append(i+2)
        if b>=1:
            a=x[b+1]
            x.append(i+a)
        if b==y-3:
            break
    x[0]=1
    return(x[y-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


