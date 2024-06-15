def Fibonacci(num,n):
    a=n-3
    f=int(a)
    for x in range(0,f):
        b=num.pop(0)
        c=num.pop(1)
        d=b+c
        num.append(c)
        num.append(d)
    e=num.pop()
    return e




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


