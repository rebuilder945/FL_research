def Fibonacci(num,n):
    a=int(n-2)
    for x in range(0,a):
        
        
        d=num[-1]+num[-2]
        
        num.append(d)
    e=num.pop()
    return e




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


