def Fibonacci(a,b):
    if b>2:
        for i in range(b-2):
                m=a[i]+a[i+1]
                a.append(m)
        return m
    elif b<2:
         return a[b-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


