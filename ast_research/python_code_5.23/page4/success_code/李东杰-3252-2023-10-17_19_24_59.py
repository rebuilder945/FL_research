def Fibonacci(num,n):
    a=n-3
    for x in range(0,a):
        b=num.pop(0)
        c=num.pop(1)
        d=b+c
        num.append(d)
        num.insert(0,c)
    e=num.pop()
    return e




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


