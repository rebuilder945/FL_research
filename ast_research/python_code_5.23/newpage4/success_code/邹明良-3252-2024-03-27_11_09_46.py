def Fibonacci(num,  a):
    m,n=1,1
    for i in range(a-2):
        m,n=n,m+n
    return n




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


