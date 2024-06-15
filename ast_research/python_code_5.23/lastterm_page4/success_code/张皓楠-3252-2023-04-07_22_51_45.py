def Fibonacci(a,n):
    if n>len(a):
        for i in range(n-len(a)):
            c = a[-1]+a[-2]
            a.append(c)
        return a[n-1]
    else:
        return a[2]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


