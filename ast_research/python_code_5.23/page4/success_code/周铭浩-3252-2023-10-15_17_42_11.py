def Fibonacci(a,n):
    for i in range(n):
        if i>=2:
            b=a[i-1]+a[i-2]
            a.append(b)
        else:
            continue
    return a[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


