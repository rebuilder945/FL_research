def Fibonacci(num,n) :
    b=n-2
    for x in range(b)
        a=num[n-3]+num[n-2]
        num.append(a)
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


