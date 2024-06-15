def Fibonacci(m,n):
    m=[1,1]
    m1=1
    m2=1
    for i in range(n-2):
        v=m1+m2
        m1=m2
        m2=v
    return v




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


