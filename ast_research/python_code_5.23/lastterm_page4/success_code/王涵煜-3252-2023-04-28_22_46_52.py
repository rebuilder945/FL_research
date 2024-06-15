def Fibonacci(x,y):
    a1=num[0]
    a2=num[1]
    for i in range(3,n+1):
        t=a1       
        a1=a1+a2
        a2=t
    return(a1)





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


