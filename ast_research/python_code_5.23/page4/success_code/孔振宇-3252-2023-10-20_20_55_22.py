def Fibonacci(a,b):
    c=eval(a[0])
    d=eval(a[1])
    b=b-2
    for i in range(b):
        c,d=d,c+d
    return(d)
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


