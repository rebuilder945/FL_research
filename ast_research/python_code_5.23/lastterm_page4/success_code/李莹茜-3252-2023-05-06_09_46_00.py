def Fibonacci(biao,shu):
    for i in range(2,shu):
        biao.append(biao[-1]+biao[-2])
    return biao[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


