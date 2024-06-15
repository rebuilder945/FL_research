def Fibonacci(num,n) :
    for i in range(2，n) :
        m=num[i-1]+num[i-2]
        num.append(m)
    return num[n]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


