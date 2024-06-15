def Fibonacci(num,n):
    a,b = 1,1
    for i in range(n-2):
        a,b = b,a+b
        ls = []
        ls.append(b)
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


