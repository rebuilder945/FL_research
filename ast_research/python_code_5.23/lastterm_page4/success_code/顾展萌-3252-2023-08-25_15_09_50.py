def Fibonacci(m,n):
    last = m[0]
    now = m[1]
    next =1
    for i in range(n):
        if n <2 :
            next = 1
        else:
            next = last+now
            last = now
            now= next
    return next




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


