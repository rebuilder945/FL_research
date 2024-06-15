def Fibonacci(a,b):
    m=n+1
    n=0
    for x in range(b-2):
        c=a[n]+a[m]
        n+=1
        a.append(c)
    return a[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


