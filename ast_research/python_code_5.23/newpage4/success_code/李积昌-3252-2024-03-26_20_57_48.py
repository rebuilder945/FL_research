def Fibonacci(num,n) :
    b=n-2
    for x in range(b) :
        a=num[x]+num[x+1]
        num.append(a)
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


