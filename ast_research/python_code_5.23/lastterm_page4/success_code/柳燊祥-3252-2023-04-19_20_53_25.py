def Fibonacci(num,n):
    i=0
    while i<=n-1:
        i=i+1
        fn=num[-1]+num[-2]
        num.append(fn)
    return num[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


