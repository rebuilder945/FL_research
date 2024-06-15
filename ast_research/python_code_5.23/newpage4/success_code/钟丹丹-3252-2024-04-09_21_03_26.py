def Fibonacci(num,  n):
    a, b=1,1
    m=[]
    for x in range(n):
        m.append(a)
        a, b=b,a+b
    return m[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


